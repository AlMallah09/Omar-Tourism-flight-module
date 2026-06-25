from sqlalchemy.orm import Session

from app.users import models, schemas
from app.authentication.utils import hash_password


def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = hash_password(user.password)

    db_user = models.User(
        full_name=user.full_name,
        email=user.email,
        phone=user.phone,
        password_hash=hashed_password,
        role="user",
    )

    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user