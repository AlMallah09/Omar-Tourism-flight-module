from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.users import schemas
from app.users.schemas import UserResponse
from app.authentication.utils import get_current_admin
from app.users.models import User
from app.users import services

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)


@router.post("/", response_model=schemas.UserResponse)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return services.create_user(db, user)
