from sqlalchemy.orm import Session

from app.users.models import User
from app.bookings.models import Booking
from app.flights.models import Flight
from app.passengers.models import Passenger
from app.admin.schemas import DashboardStats
from app.admin.models import AuditLog


def get_dashboard_stats(db: Session):
    return DashboardStats(
        total_users=db.query(User).count(),
        active_users=db.query(User).filter(User.is_active == True).count(),
        disabled_users=db.query(User).filter(User.is_active == False).count(),
        deleted_users=db.query(User).filter(User.is_deleted == True).count(),

        admins=db.query(User).filter(User.role == "admin").count(),
        regular_users=db.query(User).filter(User.role == "user").count(),

        total_bookings=db.query(Booking).count(),
        confirmed_bookings=db.query(Booking).filter(Booking.booking_status == "confirmed").count(),
        cancelled_bookings=db.query(Booking).filter(Booking.booking_status == "cancelled").count(),

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