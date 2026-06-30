from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.authentication.utils import (
    admin_required,
    get_current_admin,
    hash_password,
    verify_password,
)
from app.authentication.models import PasswordHistory
from app.authentication import services as auth_services
from app.authentication.services import validate_password_strength
from app.admin import services
from app.admin.schemas import (
    AdminResetPasswordRequest,
    AdminResetPasswordResponse,
    DashboardStats,
    BookingAdminFilter,
    PaymentStatusUpdate,
    BookingStatusUpdate,
    FlightAdminFilter,
    RecentActivity,
    AuditLogResponse,
)
from app.users.models import User
from app.users.schemas import UserResponse
from app.bookings.models import Booking
from app.bookings import schemas as booking_schemas
from app.bookings.schemas import BookingResponse
from app.bookings import services as booking_service
from app.flights.models import Flight
from app.passengers.models import Passenger


router = APIRouter(
    prefix="/admin",
    tags=["Admin"]
)

@router.get("/system-health")
def system_health(
    db: Session = Depends(get_db),
    current_admin: User = Depends(admin_required)
):
    return services.get_system_health(db)

@router.get("/dashboard", response_model=DashboardStats)
def get_dashboard(
    db: Session = Depends(get_db),
    current_admin: User = Depends(get_current_admin)
):
    return services.get_dashboard_stats(db)

@router.get("/audit-logs", response_model=list[AuditLogResponse])
def audit_logs(
    page: int = 1,
    page_size: int = 20,
    db: Session = Depends(get_db),
    current_admin: User = Depends(admin_required)
):
    return services.get_audit_logs(db, page, page_size)

@router.get("/recent-activity", response_model=RecentActivity)
def recent_activity(
    db: Session = Depends(get_db),
    current_admin: User = Depends(admin_required)
):
    return services.get_recent_activity(db)

@router.get("/users", response_model=list[UserResponse])
def get_all_users(
    db: Session = Depends(get_db),
    current_admin: User = Depends(get_current_admin)
):
    users = db.query(User).all()
    return users


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

@router.post("/bookings/filter", response_model=list[BookingResponse])
def filter_bookings(
    filters: BookingAdminFilter,
    page: int = 1,
    page_size: int = 20,
    db: Session = Depends(get_db),
    current_admin: User = Depends(admin_required)
):
    return services.filter_bookings_admin(db, filters, page, page_size)

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

@router.put("/bookings/{booking_id}/payment-status", response_model=BookingResponse)
def update_payment_status(
    booking_id: int,
    status_update: PaymentStatusUpdate,
    db: Session = Depends(get_db),
    current_admin: User = Depends(admin_required)
):
    return services.update_booking_payment_status_admin(
        db,
        booking_id,
        status_update.payment_status
    )

@router.put("/bookings/{booking_id}/status", response_model=BookingResponse)
def update_booking_status(
    booking_id: int,
    status_update: BookingStatusUpdate,
    db: Session = Depends(get_db),
    current_admin: User = Depends(admin_required)
):
    return services.update_booking_status_admin(
        db,
        booking_id,
        status_update.booking_status
    )

@router.put("/users/{user_id}/reset-password",response_model=AdminResetPasswordResponse)
def reset_user_password_admin(
    user_id: int,
    password_data: AdminResetPasswordRequest,
    db: Session = Depends(get_db),
    current_admin: User = Depends(get_current_admin)
):
    user = db.query(User).filter(User.user_id == user_id).first()

    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    validate_password_strength(password_data.new_password)

    password_history = (
    db.query(PasswordHistory)
    .filter(PasswordHistory.user_id == user.user_id)
    .order_by(PasswordHistory.changed_at.desc())
    .limit(5)
    .all()
)

    for old_password in password_history:
        if verify_password(password_data.new_password, old_password.password_hash):
            raise HTTPException(
                status_code=400,
                detail="You cannot reuse a previously used password."
        )
    
    history = PasswordHistory(
    user_id=user.user_id,
    password_hash=user.password_hash
)

    db.add(history)

    user.password_hash = hash_password(password_data.new_password)
    user.must_change_password = True
    user.failed_login_attempts = 0
    user.account_locked = False

    db.commit()
    db.refresh(user)

    services.create_audit_log(
        db=db,
        admin_id=current_admin.user_id,
        action="ADMIN_RESET_PASSWORD",
        target_type="User",
        target_id=user.user_id,
        description=f"Admin reset password for user: {user.email}"
    )

    return {"message": "Password reset successfully. User must change password on next login."}

@router.put("/users/{user_id}/unlock", response_model=UserResponse)
def unlock_user_account_admin(
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

    user.account_locked = False
    user.failed_login_attempts = 0

    db.commit()
    db.refresh(user)

    services.create_audit_log(
        db=db,
        admin_id=current_admin.user_id,
        action="UNLOCK_USER_ACCOUNT",
        target_type="User",
        target_id=user.user_id,
        description=f"Unlocked user account: {user.email}"
    )

    return user

@router.delete("/password-reset-tokens/expired")
def cleanup_expired_reset_tokens_admin(
    db: Session = Depends(get_db),
    current_admin: User = Depends(get_current_admin)
):
    result = auth_services.cleanup_expired_reset_tokens(db)

    services.create_audit_log(
        db=db,
        admin_id=current_admin.user_id,
        action="CLEANUP_EXPIRED_RESET_TOKENS",
        target_type="PasswordResetToken",
        target_id=0,
        description="Cleaned expired password reset tokens."
    )

    return result