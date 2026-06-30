from warnings import filters
from fastapi import HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import text
from app.users.models import User
from app.bookings.models import Booking
from app.flights.models import Flight
from app.passengers.models import Passenger
from app.admin.schemas import DashboardStats
from app.admin.models import AuditLog
from app.admin.schemas import BookingAdminFilter
from app.core.constants import BookingStatus, PaymentStatus, FlightStatus

def get_system_health(db: Session):
    try:
        db.execute(text("SELECT 1"))

        return {
            "api_status": "online",
            "database_status": "connected",
            "system_status": "healthy"
        }

    except Exception:
        return {
            "api_status": "online",
            "database_status": "disconnected",
            "system_status": "unhealthy"
        }

def get_dashboard_stats(db: Session):
    return DashboardStats(
        total_users=db.query(User).count(),
        active_users=db.query(User).filter(User.is_active == True).count(),
        disabled_users=db.query(User).filter(User.is_active == False).count(),
        deleted_users=db.query(User).filter(User.is_deleted == True).count(),
        admins=db.query(User).filter(User.role == "admin").count(),
        regular_users=db.query(User).filter(User.role == "user").count(),
        total_bookings=db.query(Booking).count(),
        confirmed_bookings=db.query(Booking).filter(Booking.booking_status == BookingStatus.CONFIRMED).count(),
        cancelled_bookings=db.query(Booking).filter(Booking.booking_status == BookingStatus.CANCELLED).count(),
        paid_bookings=db.query(Booking).filter(Booking.payment_status == PaymentStatus.PAID).count(),
        unpaid_bookings=db.query(Booking).filter(Booking.payment_status == PaymentStatus.UNPAID).count(),
        refunded_bookings=db.query(Booking).filter(Booking.payment_status == PaymentStatus.REFUNDED).count(),
        pending_payments=db.query(Booking).filter(Booking.payment_status == PaymentStatus.PENDING).count(),
        failed_payments=db.query(Booking).filter(Booking.payment_status == PaymentStatus.FAILED).count(),
        total_flights=db.query(Flight).count(),
        total_passengers=db.query(Passenger).count(),
    )

def create_audit_log(
    db: Session,
    admin_id: int,
    action: str,
    target_type: str,
    target_id: int,
    description: str
):
    log = AuditLog(
        admin_id=admin_id,
        action=action,
        target_type=target_type,
        target_id=target_id,
        description=description
    )

    db.add(log)
    db.commit()
    db.refresh(log)

    return log

def get_audit_logs(db: Session, page: int = 1, page_size: int = 20):
    if page < 1:
        page = 1

    if page_size < 1:
        page_size = 20

    if page_size > 100:
        page_size = 100

    offset = (page - 1) * page_size

    return (
        db.query(AuditLog)
        .order_by(AuditLog.timestamp.desc())
        .offset(offset)
        .limit(page_size)
        .all()
    )

def filter_bookings_admin(db: Session, filters: BookingAdminFilter, page: int = 1, page_size: int = 20):
    query = db.query(Booking)

    if filters.user_id is not None:
        query = query.filter(Booking.user_id == filters.user_id)

    if filters.flight_id is not None:
        query = query.filter(Booking.flight_id == filters.flight_id)

    if filters.booking_status is not None:
        query = query.filter(Booking.booking_status == filters.booking_status)

    if filters.payment_status is not None:
        query = query.filter(Booking.payment_status == filters.payment_status)

    if filters.min_total_price is not None:
        query = query.filter(Booking.total_price >= filters.min_total_price)

    if filters.max_total_price is not None:
        query = query.filter(Booking.total_price <= filters.max_total_price)

    if page < 1:
       page = 1

    if page_size < 1:
       page_size = 20

    if page_size > 100:
       page_size = 100

    offset = (page - 1) * page_size

    return (
        query.order_by(Booking.booking_id.desc())
        .offset(offset)
        .limit(page_size)
        .all()
)

def update_booking_payment_status_admin(
    db: Session,
    booking_id: int,
    payment_status: str
):
    booking = db.query(Booking).filter(Booking.booking_id == booking_id).first()

    if not booking:
        raise HTTPException(status_code=404, detail="Booking not found")

    new_payment_status = payment_status.value if hasattr(payment_status, "value") else payment_status
    new_payment_status = new_payment_status.lower()
    booking_status = booking.booking_status.lower()

    allowed_statuses = [
        PaymentStatus.UNPAID,
        PaymentStatus.PENDING,
        PaymentStatus.PAID,
        PaymentStatus.FAILED,
        PaymentStatus.REFUNDED
    ]

    if new_payment_status not in allowed_statuses:
        raise HTTPException(status_code=400, detail="Invalid payment status")

    if booking_status == BookingStatus.CONFIRMED:
        allowed_for_confirmed = [
            PaymentStatus.UNPAID,
            PaymentStatus.PENDING,
            PaymentStatus.PAID,
            PaymentStatus.FAILED
        ]

        if new_payment_status not in allowed_for_confirmed:
            raise HTTPException(
                status_code=400,
                detail="Confirmed bookings cannot have this payment status"
            )

    if booking_status == BookingStatus.CANCELLED:
        allowed_for_cancelled = [
            PaymentStatus.UNPAID,
            PaymentStatus.FAILED,
            PaymentStatus.REFUNDED
        ]

        if new_payment_status not in allowed_for_cancelled:
            raise HTTPException(
                status_code=400,
                detail="Cancelled bookings can only be unpaid, failed, or refunded"
            )

    booking.payment_status = new_payment_status

    db.commit()
    db.refresh(booking)

    return booking

def update_booking_status_admin(
    db: Session,
    booking_id: int,
    booking_status: str
):
    booking = db.query(Booking).filter(Booking.booking_id == booking_id).first()

    if not booking:
        raise HTTPException(status_code=404, detail="Booking not found")

    allowed_statuses = [BookingStatus.CONFIRMED, BookingStatus.CANCELLED]

    new_booking_status = booking_status.value if hasattr(booking_status, "value") else booking_status
    new_booking_status = new_booking_status.lower()

    if new_booking_status not in allowed_statuses:
        raise HTTPException(
            status_code=400,
            detail="Invalid booking status"
        )

    booking.booking_status = new_booking_status

    db.commit()
    db.refresh(booking)

    return booking

def get_recent_activity(db: Session):
    recent_users = (
        db.query(User)
        .order_by(User.user_id.desc())
        .limit(5)
        .all()
    )

    recent_bookings = (
        db.query(Booking)
        .order_by(Booking.booking_id.desc())
        .limit(5)
        .all()
    )

    recent_flights = (
        db.query(Flight)
        .order_by(Flight.flight_id.desc())
        .limit(5)
        .all()
    )

    return {
        "recent_users": recent_users,
        "recent_bookings": recent_bookings,
        "recent_flights": recent_flights
    }