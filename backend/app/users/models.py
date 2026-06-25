from sqlalchemy import Column, Integer, String, DateTime, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.db.base import Base


class User(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    phone = Column(String, nullable=True)
    password_hash = Column(String, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    role = Column(String, default="user")
    is_active = Column(Boolean, default=True)
    is_deleted = Column(Boolean, default=False)
    must_change_password = Column(Boolean, default=False)
    failed_login_attempts = Column(Integer, default=0)
    account_locked = Column(Boolean, default=False)
    last_login = Column(DateTime, nullable=True)
    password_changed_at = Column(DateTime, nullable=True)

    bookings = relationship("Booking", back_populates="user")