from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.bookings import models, schemas
from app.flights.models import Flight
from app.bookings.models import Booking
from app.core.constants import BookingStatus, PaymentStatus, FlightStatus


def create_booking(db: Session, booking: schemas.BookingCreate, user_id: int):
    flight = db.query(Flight).filter(
        Flight.flight_id == booking.flight_id
    ).first()

    if not flight:
        raise HTTPException(status_code=404, detail="Flight not found")

    if flight.status.lower() == BookingStatus.CANCELLED:
        raise HTTPException(status_code=400, detail="Cannot book a cancelled flight")

    if flight.seats_available < booking.number_of_passengers:
        raise HTTPException(status_code=400, detail="Not enough seats available")

    total_price = flight.price * booking.number_of_passengers

    db_booking = models.Booking(
    user_id=user_id,
    flight_id=booking.flight_id,
    number_of_passengers=booking.number_of_passengers,
    total_price=total_price,
    booking_status=BookingStatus.CONFIRMED,
    payment_status=PaymentStatus.UNPAID
)

    flight.seats_available -= booking.number_of_passengers

    db.add(db_booking)
    db.commit()
    db.refresh(db_booking)

    return db_booking

def get_bookings_by_user(db: Session, user_id: int):
    return db.query(models.Booking).filter(
        models.Booking.user_id == user_id
    ).all()

from app.flights.models import Flight


def cancel_booking(db: Session, booking_id: int):
    booking = db.query(models.Booking).filter(
        models.Booking.booking_id == booking_id
    ).first()

    if not booking:
        raise HTTPException(status_code=404, detail="Booking not found")

    if booking.booking_status == BookingStatus.CANCELLED:
        raise HTTPException(status_code=400, detail="Booking is already cancelled")

    flight = db.query(Flight).filter(
        Flight.flight_id == booking.flight_id
    ).first()

    flight.seats_available += booking.number_of_passengers
    booking.booking_status = BookingStatus.CANCELLED

    db.commit()
    db.refresh(booking)

    return booking

def restore_booking(db: Session, booking_id: int):
    booking = db.query(Booking).filter(
        Booking.booking_id == booking_id
    ).first()

    if not booking:
        raise HTTPException(
            status_code=404,
            detail="Booking not found"
        )

    if booking.booking_status != BookingStatus.CANCELLED:
        raise HTTPException(
            status_code=400,
            detail="Booking is not cancelled"
        )

    flight = db.query(Flight).filter(
        Flight.flight_id == booking.flight_id
    ).first()

    if not flight:
        raise HTTPException(
            status_code=404,
            detail="Flight not found"
        )

    if flight.seats_available <= 0:
        raise HTTPException(
            status_code=400,
            detail="No seats available to restore this booking"
        )

    booking.booking_status = BookingStatus.CONFIRMED
    flight.seats_available -= 1

    db.commit()
    db.refresh(booking)

    return booking

def get_my_bookings(db: Session, user_id: int):
    return db.query(models.Booking).filter(
        models.Booking.user_id == user_id
    ).all()

def get_booking_details(
    db: Session,
    booking_id: int,
    user_id: int
):
    booking = db.query(models.Booking).filter(
        models.Booking.booking_id == booking_id,
        models.Booking.user_id == user_id
    ).first()

    if not booking:
        raise HTTPException(status_code=404, detail="Booking not found")

    return booking