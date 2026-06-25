from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime


class UserBase(BaseModel):
    full_name: str
    email: EmailStr
    phone: Optional[str] = None


class UserCreate(UserBase):
    password: str


class UserResponse(UserBase):
    user_id: int
    created_at: datetime
    role: str
    is_active: bool
    is_deleted: bool
    must_change_password: bool
    account_locked: bool
    last_login: datetime | None
    password_changed_at: datetime | None

    class Config:
        from_attributes = True