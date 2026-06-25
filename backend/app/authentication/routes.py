from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.users.models import User
from app.users.schemas import UserResponse
from app.authentication.utils import get_current_admin
from app.authentication.utils import verify_password, create_access_token
from app.authentication import schemas
from app.bookings.models import Booking
from app.flights.models import Flight
from app.passengers.models import Passenger


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

    if not verify_password(form_data.password, user.password_hash):
        raise HTTPException(status_code=401, detail="Invalid email or password")

    if user.is_deleted:
        raise HTTPException(status_code=403, detail="Account has been deleted. Please contact support.")

    if not user.is_active:
        raise HTTPException(status_code=403, detail="Account is disabled. Please contact support.")

    access_token = create_access_token(
        data={"sub": user.email}
    )

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }

@router.get("/admin/users", response_model=list[UserResponse])
def get_all_users(
    db: Session = Depends(get_db),
    current_admin: User = Depends(get_current_admin)
):
    return db.query(User).all()

