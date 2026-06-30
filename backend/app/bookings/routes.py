from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.bookings.models import Booking
from app.db.database import get_db
from app.bookings import schemas
from app.authentication.utils import admin_required, get_current_user
from app.authentication.utils import get_current_admin
from app.users.models import User
from app.bookings import services


router = APIRouter(
    prefix="/bookings",
    tags=["Bookings"]
)


@router.post("/", response_model=schemas.BookingResponse)
def create_booking(
    booking: schemas.BookingCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(admin_required)
):
    return services.create_booking(
        db,
        booking,
        current_user.user_id
    )

@router.get("/me", response_model=list[schemas.BookingResponse])
def get_my_bookings(
    db: Session = Depends(get_db),
    current_user: User = Depends(admin_required)
):
    return services.get_my_bookings(
        db,
        current_user.user_id
    )

@router.get("/user/{user_id}", response_model=list[schemas.BookingResponse])
def get_bookings_by_user(
    user_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(admin_required)
):
    if current_user.user_id != user_id:
        raise HTTPException(
            status_code=403,
            detail="Not allowed to view another user's bookings"
        )

    return services.get_bookings_by_user(db, user_id)

@router.put("/{booking_id}/cancel", response_model=schemas.BookingResponse)
def cancel_booking(
    booking_id: int,
    db: Session = Depends(get_db)
):
    return services.cancel_booking(db, booking_id)

@router.get("/{booking_id}/details",response_model=schemas.BookingDetailsResponse)
def get_booking_details(
    booking_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(admin_required)
):
    return services.get_booking_details(
        db=db,
        booking_id=booking_id,
        user_id=current_user.user_id
    )

