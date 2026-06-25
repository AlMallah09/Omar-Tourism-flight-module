from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.authentication.utils import get_current_admin

from app.admin.schemas import DashboardStats
from app.admin import services

from app.users.models import User
from app.bookings.models import Booking
from app.flights.models import Flight
from app.passengers.models import Passenger
from app.users.schemas import UserResponse
from app.bookings import schemas, service
from app.bookings.models import Booking
from app.bookings import schemas as booking_schemas
from app.bookings import service as booking_service

router = APIRouter(
    prefix="/admin",
    tags=["Admin"]
)

@router.get("/dashboard", response_model=DashboardStats)
def get_dashboard(
    db: Session = Depends(get_db),
    current_admin: User = Depends(get_current_admin)
):
    return services.get_dashboard_stats(db)


@router.get("/users/search", response_model=list[UserResponse])
def search_users_admin(
    query: str,
    db: Session = Depends(get_db),
    current_admin: User = Depends(get_current_admin)
):
    users = db.query(User).filter(
        (User.full_name.ilike(f"%{query}%")) |
        (User.email.ilike(f"%{query}%"))
    ).all()

    return users

@router.get("/users/{user_id}", response_model=UserResponse)
def get_user_by_id_admin(
    user_id: int,
    db: Session = Depends(get_db),
    current_admin: User = Depends(get_current_admin)
):
    user = db.query(User).filter(
        User.user_id == user_id
    ).first()

    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    return user

@router.put("/users/{user_id}/role", response_model=UserResponse)
def change_user_role_admin(
    user_id: int,
    role: str,
    db: Session = Depends(get_db),
    current_admin: User = Depends(get_current_admin)
):
    if role not in ["user", "admin"]:
        raise HTTPException(
            status_code=400,
            detail="Invalid role. Role must be 'user' or 'admin'"
        )

    user = db.query(User).filter(User.user_id == user_id).first()

    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    old_role = user.role
    user.role = role
    db.commit()
    db.refresh(user)

    services.create_audit_log(
    db=db,
    admin_id=current_admin.user_id,
    action="CHANGE_USER_ROLE",
    target_type="User",
    target_id=user.user_id,
    description=f"Changed user role from {old_role} to {user.role}"
)

    return user

@router.put("/users/{user_id}/disable", response_model=UserResponse)
def disable_user_admin(
    user_id: int,
    db: Session = Depends(get_db),
    current_admin: User = Depends(get_current_admin)
):
    user = db.query(User).filter(User.user_id == user_id).first()

    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    user.is_active = False
    db.commit()
    db.refresh(user)

    services.create_audit_log(
    db=db,
    admin_id=current_admin.user_id,
    action="DISABLE_USER",
    target_type="User",
    target_id=user.user_id,
    description=f"Disabled user account: {user.email}"
)

    return user

@router.put("/users/{user_id}/enable", response_model=UserResponse)
def enable_user_admin(
    user_id: int,
    db: Session = Depends(get_db),
    current_admin: User = Depends(get_current_admin)
):
    user = db.query(User).filter(User.user_id == user_id).first()

    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    user.is_active = True
    db.commit()
    db.refresh(user)

    services.create_audit_log(
    db=db,
    admin_id=current_admin.user_id,
    action="ENABLE_USER",
    target_type="User",
    target_id=user.user_id,
    description=f"Enabled user account: {user.email}"
)

    return user

@router.put("/users/{user_id}/delete", response_model=UserResponse)
def soft_delete_user_admin(
    user_id: int,
    db: Session = Depends(get_db),
    current_admin: User = Depends(get_current_admin)
):
    user = db.query(User).filter(User.user_id == user_id).first()

    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    user.is_deleted = True
    user.is_active = False

    db.commit()
    db.refresh(user)

    services.create_audit_log(
    db=db,
    admin_id=current_admin.user_id,
    action="SOFT_DELETE_USER",
    target_type="User",
    target_id=user.user_id,
    description=f"Soft deleted user account: {user.email}"
)

    return user

@router.put("/users/{user_id}/restore", response_model=UserResponse)
def restore_user_admin(
    user_id: int,
    db: Session = Depends(get_db),
    current_admin: User = Depends(get_current_admin)
):
    user = db.query(User).filter(User.user_id == user_id).first()

    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    user.is_deleted = False
    user.is_active = True

    db.commit()
    db.refresh(user)

    services.create_audit_log(
    db=db,
    admin_id=current_admin.user_id,
    action="RESTORE_USER",
    target_type="User",
    target_id=user.user_id,
    description=f"Restored user account: {user.email}"
)

    return user

@router.get("/bookings")
def get_all_bookings_admin(
    db: Session = Depends(get_db),
    current_admin: User = Depends(get_current_admin)
):
    return db.query(Booking).all()

@router.get("/bookings/{booking_id}")
def get_booking_by_id_admin(
    booking_id: int,
    db: Session = Depends(get_db),
    current_admin: User = Depends(get_current_admin)
):
    booking = db.query(Booking).filter(
        Booking.booking_id == booking_id
    ).first()

    if not booking:
        raise HTTPException(
            status_code=404,
            detail="Booking not found"
        )

    return booking

@router.put("/bookings/{booking_id}/cancel", response_model=booking_schemas.BookingResponse)
def cancel_booking_admin(
    booking_id: int,
    db: Session = Depends(get_db),
    current_admin: User = Depends(get_current_admin)
):
    booking = booking_service.cancel_booking(db, booking_id)

    services.create_audit_log(
    db=db,
    admin_id=current_admin.user_id,
    action="CANCEL_BOOKING",
    target_type="Booking",
    target_id=booking.booking_id,
    description=f"Cancelled booking ID {booking.booking_id}"
)
    
    return booking

@router.put("/bookings/{booking_id}/restore", response_model=booking_schemas.BookingResponse)
def restore_booking_admin(
    booking_id: int,
    db: Session = Depends(get_db),
    current_admin: User = Depends(get_current_admin)
):
    booking = booking_service.restore_booking(db, booking_id)

    services.create_audit_log(
    db=db,
    admin_id=current_admin.user_id,
    action="RESTORE_BOOKING",
    target_type="Booking",
    target_id=booking.booking_id,
    description=f"Restored booking ID {booking.booking_id}"
)
    
    return booking

