from sqlalchemy import func
from sqlalchemy.orm import Session

from app.bookings.models import Booking
from app.core.constants import BookingStatus, PaymentStatus
from app.flights.models import Flight
from app.core.constants import FlightStatus
from app.users.models import User

def get_revenue_analytics(db: Session):
    total_revenue = db.query(
        func.coalesce(func.sum(Booking.total_price), 0)
    ).scalar()

    paid_revenue = db.query(
        func.coalesce(func.sum(Booking.total_price), 0)
    ).filter(
        Booking.payment_status == PaymentStatus.PAID
    ).scalar()

    refunded_amount = db.query(
        func.coalesce(func.sum(Booking.total_price), 0)
    ).filter(
        Booking.payment_status == PaymentStatus.REFUNDED
    ).scalar()

    average_booking_value = db.query(
        func.coalesce(func.avg(Booking.total_price), 0)
    ).scalar()

    return {
        "total_revenue": float(total_revenue),
        "paid_revenue": float(paid_revenue),
        "refunded_amount": float(refunded_amount),
        "average_booking_value": float(average_booking_value)
    }


def get_booking_analytics(db: Session):
    total_bookings = db.query(Booking).count()

    confirmed_bookings = db.query(Booking).filter(
        Booking.booking_status == BookingStatus.CONFIRMED
    ).count()

    cancelled_bookings = db.query(Booking).filter(
        Booking.booking_status == BookingStatus.CANCELLED
    ).count()

    paid_bookings = db.query(Booking).filter(
        Booking.payment_status == PaymentStatus.PAID
    ).count()

    refunded_bookings = db.query(Booking).filter(
        Booking.payment_status == PaymentStatus.REFUNDED
    ).count()

    cancellation_rate = (
        (cancelled_bookings / total_bookings) * 100
        if total_bookings > 0
        else 0
    )

    return {
        "total_bookings": total_bookings,
        "confirmed_bookings": confirmed_bookings,
        "cancelled_bookings": cancelled_bookings,
        "paid_bookings": paid_bookings,
        "refunded_bookings": refunded_bookings,
        "cancellation_rate": round(cancellation_rate, 2)
    }


def get_flight_analytics(db: Session):
    total_flights = db.query(Flight).count()

    active_flights = db.query(Flight).filter(
        Flight.status != FlightStatus.CANCELLED
    ).count()

    cancelled_flights = db.query(Flight).filter(
        Flight.status == FlightStatus.CANCELLED
    ).count()

    total_seats_available = db.query(
        func.coalesce(func.sum(Flight.seats_available), 0)
    ).scalar()

    total_bookings = db.query(Booking).count()

    average_bookings_per_flight = (
        total_bookings / total_flights
        if total_flights > 0
        else 0
    )

    return {
        "total_flights": total_flights,
        "active_flights": active_flights,
        "cancelled_flights": cancelled_flights,
        "total_seats_available": int(total_seats_available),
        "total_bookings": total_bookings,
        "average_bookings_per_flight": round(
            average_bookings_per_flight, 2
        )
    }


def get_top_destinations(db: Session):
    results = (
        db.query(
            Flight.destination,
            func.count(Booking.booking_id).label("bookings")
        )
        .join(Booking, Booking.flight_id == Flight.flight_id)
        .group_by(Flight.destination)
        .order_by(func.count(Booking.booking_id).desc())
        .limit(10)
        .all()
    )

    return [
        {
            "destination": destination,
            "bookings": bookings
        }
        for destination, bookings in results
    ]

def get_top_origins(db: Session):
    results = (
        db.query(
            Flight.origin,
            func.count(Booking.booking_id).label("bookings")
        )
        .join(Booking, Booking.flight_id == Flight.flight_id)
        .group_by(Flight.origin)
        .order_by(func.count(Booking.booking_id).desc())
        .limit(10)
        .all()
    )

    return [
        {
            "origin": origin,
            "bookings": bookings
        }
        for origin, bookings in results
    ]

def get_top_routes(db: Session):
    results = (
        db.query(
            Flight.origin,
            Flight.destination,
            func.count(Booking.booking_id).label("bookings")
        )
        .join(Booking, Booking.flight_id == Flight.flight_id)
        .group_by(
            Flight.origin,
            Flight.destination
        )
        .order_by(func.count(Booking.booking_id).desc())
        .limit(10)
        .all()
    )

    return [
        {
            "origin": origin,
            "destination": destination,
            "bookings": bookings
        }
        for origin, destination, bookings in results
    ]


def get_customer_analytics(db: Session):
    total_customers = (
        db.query(User)
        .filter(User.role == "user")
        .count()
    )

    customers_with_bookings = (
        db.query(User.user_id)
        .join(
            Booking,
            Booking.user_id == User.user_id
        )
        .filter(
            User.role == "user"
        )
        .distinct()
        .count()
    )

    customers_without_bookings = (
        total_customers - customers_with_bookings
    )

    total_bookings = (
        db.query(Booking)
        .join(
            User,
            Booking.user_id == User.user_id
        )
        .filter(
            User.role == "user"
        )
        .count()
    )

    average_bookings_per_customer = (
        total_bookings / total_customers
        if total_customers > 0
        else 0
    )

    return {
        "total_customers": total_customers,
        "customers_with_bookings": customers_with_bookings,
        "customers_without_bookings": customers_without_bookings,
        "average_bookings_per_customer": round(
            average_bookings_per_customer,
            2
        )
    }

def get_top_customers(db: Session):
    results = (
        db.query(
            User.user_id,
            User.email,
            func.count(Booking.booking_id).label("bookings"),
            func.coalesce(
                func.sum(Booking.total_price), 0
            ).label("total_spent")
        )
        .join(
            Booking,
            Booking.user_id == User.user_id
        )
        .filter(
            User.role == "user"
        )
        .group_by(
            User.user_id,
            User.email
        )
        .order_by(
            func.sum(Booking.total_price).desc()
        )
        .limit(10)
        .all()
    )

    return [
        {
            "user_id": user_id,
            "email": email,
            "bookings": bookings,
            "total_spent": float(total_spent)
        }
        for user_id, email, bookings, total_spent in results
    ]


def get_analytics_dashboard(db: Session):
    revenue = get_revenue_analytics(db)
    bookings = get_booking_analytics(db)
    flights = get_flight_analytics(db)
    customers = get_customer_analytics(db)

    return {
        "total_revenue": revenue["total_revenue"],
        "paid_revenue": revenue["paid_revenue"],
        "refunded_amount": revenue["refunded_amount"],
        "average_booking_value": revenue["average_booking_value"],

        "total_bookings": bookings["total_bookings"],
        "confirmed_bookings": bookings["confirmed_bookings"],
        "cancelled_bookings": bookings["cancelled_bookings"],
        "cancellation_rate": bookings["cancellation_rate"],

        "total_flights": flights["total_flights"],
        "active_flights": flights["active_flights"],
        "cancelled_flights": flights["cancelled_flights"],

        "total_customers": customers["total_customers"],
        "customers_with_bookings": customers["customers_with_bookings"],
        "customers_without_bookings": customers["customers_without_bookings"]
    }


def get_monthly_analytics(db: Session):
    results = (
        db.query(
            func.date_trunc("month", Booking.booking_date).label("month"),
            func.count(Booking.booking_id).label("bookings"),
            func.coalesce(
                func.sum(Booking.total_price),
                0
            ).label("revenue")
        )
        .group_by(
            func.date_trunc("month", Booking.booking_date)
        )
        .order_by(
            func.date_trunc("month", Booking.booking_date)
        )
        .all()
    )

    return [
        {
            "month": month.strftime("%Y-%m"),
            "bookings": bookings,
            "revenue": float(revenue)
        }
        for month, bookings, revenue in results
    ]


def get_top_flights(db: Session):
    results = (
        db.query(
            Flight.flight_id,
            Flight.airline,
            Flight.origin,
            Flight.destination,
            func.count(Booking.booking_id).label("confirmed_bookings"),
            func.coalesce(
                func.sum(Booking.number_of_passengers),
                0
            ).label("passengers_booked")
        )
        .join(
            Booking,
            Booking.flight_id == Flight.flight_id
        )
        .filter(
            Booking.booking_status == BookingStatus.CONFIRMED
        )
        .group_by(
            Flight.flight_id,
            Flight.airline,
            Flight.origin,
            Flight.destination
        )
        .order_by(
            func.sum(Booking.number_of_passengers).desc()
        )
        .limit(10)
        .all()
    )

    return [
        {
            "flight_id": flight_id,
            "airline": airline,
            "origin": origin,
            "destination": destination,
            "confirmed_bookings": confirmed_bookings,
            "passengers_booked": int(passengers_booked)
        }
        for (
            flight_id,
            airline,
            origin,
            destination,
            confirmed_bookings,
            passengers_booked
        ) in results
    ]


def get_customer_growth(db: Session):
    results = (
        db.query(
            func.date_trunc("month", User.created_at).label("month"),
            func.count(User.user_id).label("new_customers")
        )
        .filter(
            User.role == "user"
        )
        .group_by(
            func.date_trunc("month", User.created_at)
        )
        .order_by(
            func.date_trunc("month", User.created_at)
        )
        .all()
    )

    return [
        {
            "month": month.strftime("%Y-%m"),
            "new_customers": new_customers
        }
        for month, new_customers in results
    ]


def get_kpi_analytics(db: Session):
    revenue = get_revenue_analytics(db)
    bookings = get_booking_analytics(db)
    flights = get_flight_analytics(db)
    customers = get_customer_analytics(db)

    return {
        "paid_revenue": revenue["paid_revenue"],
        "total_bookings": bookings["total_bookings"],
        "cancellation_rate": bookings["cancellation_rate"],
        "active_flights": flights["active_flights"],
        "total_customers": customers["total_customers"],
        "customers_with_bookings": customers["customers_with_bookings"]
    }


def get_flight_occupancy(db: Session):
    flights = db.query(Flight).all()

    results = []

    for flight in flights:
        booked_seats = flight.total_seats - flight.seats_available

        occupancy_rate = (
            (booked_seats / flight.total_seats) * 100
            if flight.total_seats > 0
            else 0
        )

        results.append({
            "flight_id": flight.flight_id,
            "airline": flight.airline,
            "origin": flight.origin,
            "destination": flight.destination,
            "total_seats": flight.total_seats,
            "seats_available": flight.seats_available,
            "booked_seats": booked_seats,
            "occupancy_rate": round(occupancy_rate, 2)
        })

    return sorted(
        results,
        key=lambda x: x["occupancy_rate"],
        reverse=True
    )