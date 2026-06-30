from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from datetime import datetime
from app.db.database import get_db
from app.users.models import User
from app.users.schemas import UserResponse
from app.authentication.utils import admin_required, get_current_admin, get_current_user
from app.authentication.utils import verify_password, create_access_token
from app.authentication import schemas
from app.bookings.models import Booking
from app.flights.models import Flight
from app.passengers.models import Passenger
from app.authentication import services as auth_services


router = APIRouter(
    prefix="/authentication",
    tags=["Authentication"]
)


@router.post("/login", response_model=schemas.TokenResponse)
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):
    user = db.query(User).filter(
        User.email == form_data.username
    ).first()

    if not user:
        raise HTTPException(status_code=401, detail="Invalid email or password")

    if user.account_locked:
        raise HTTPException(
            status_code=403,
            detail="Account is locked. Please contact an administrator."
    )

    if not verify_password(form_data.password, user.password_hash):

        user.failed_login_attempts += 1

        if user.failed_login_attempts >= 5:
            user.account_locked = True

        db.commit()

        raise HTTPException(
            status_code=401,
            detail="Invalid email or password"
    )

    if user.is_deleted:
        raise HTTPException(status_code=403, detail="Account has been deleted. Please contact support.")

    if not user.is_active:
        raise HTTPException(status_code=403, detail="Account is disabled. Please contact support.")

    user.last_login = datetime.utcnow()
    user.failed_login_attempts = 0
    db.commit()
    db.refresh(user)

    access_token = create_access_token(
        data={"sub": user.email}
    )

    return {
        "access_token": access_token,
        "token_type": "bearer",
        "must_change_password": user.must_change_password
    }

@router.get("/admin/users", response_model=list[UserResponse])
def get_all_users(
    db: Session = Depends(get_db),
    current_admin: User = Depends(get_current_admin)
):
    return db.query(User).all()


@router.put("/change-password",response_model=schemas.ChangePasswordResponse)
def change_password(
    password_data: schemas.ChangePasswordRequest,
    db: Session = Depends(get_db),
    current_user: User = Depends(admin_required)
):
        return auth_services.change_password(
        db=db,
        user=current_user,
        current_password=password_data.current_password,
        new_password=password_data.new_password
    )

@router.post("/forgot-password",response_model=schemas.ForgotPasswordResponse)
def forgot_password(
    request: schemas.ForgotPasswordRequest,
    db: Session = Depends(get_db)
):
    return auth_services.forgot_password(
        db=db,
        email=request.email
    )

@router.post(
    "/reset-password",
    response_model=schemas.ResetPasswordResponse
)
def reset_password(
    request: schemas.ResetPasswordRequest,
    db: Session = Depends(get_db)
):
    return auth_services.reset_password(
        db=db,
        token=request.token,
        new_password=request.new_password
    )