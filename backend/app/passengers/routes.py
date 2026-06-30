from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.passengers.schemas import PassengerCreate, PassengerResponse
from app.passengers.services import create_passenger, get_passengers_by_booking
from app.authentication.utils import admin_required, get_current_user
from app.users.models import User
from app.bookings.models import Booking

router = APIRouter(
    prefix="/passengers",
    tags=["Passengers"]
)


@router.post(
    "/booking/{booking_id}",
    response_model=PassengerResponse
)
def add_passenger_to_booking(
    booking_id: int,
    passenger_data: PassengerCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(admin_required)
):
    booking = db.query(Booking).filter(
        Booking.booking_id == booking_id,
        Booking.user_id == current_user.user_id
    ).first()

    if not booking:
        raise HTTPException(
            status_code=403,
            detail="Not allowed to add passengers to this booking"
        )

    if booking.booking_status == "cancelled":
        raise HTTPException(
            status_code=400,
            detail="Cannot add passengers to a cancelled booking"
        )

    return create_passenger(
        db=db,
        booking_id=booking_id,
        passenger_data=passenger_data
    )

@router.get(
    "/booking/{booking_id}",
    response_model=list[PassengerResponse]
)
def list_passengers_for_booking(
    booking_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(admin_required)
):
    booking = db.query(Booking).filter(
        Booking.booking_id == booking_id,
        Booking.user_id == current_user.user_id
    ).first()

    if not booking:
        raise HTTPException(
            status_code=403,
            detail="Not allowed to view passengers for this booking"
        )

    return get_passengers_by_booking(
        db=db,
        booking_id=booking_id
    )