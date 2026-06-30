from pydantic import BaseModel
from typing import Optional
from app.bookings.schemas import BookingResponse
from app.flights.schemas import FlightResponse
from app.users.schemas import UserResponse
from datetime import datetime
from app.core.constants import BookingStatus, PaymentStatus, FlightStatus

class DashboardStats(BaseModel):
    total_users: int
    active_users: int
    disabled_users: int
    deleted_users: int
    admins: int
    regular_users: int 
    total_bookings: int
    confirmed_bookings: int
    cancelled_bookings: int
    paid_bookings: int
    unpaid_bookings: int
    refunded_bookings: int
    pending_payments: int
    failed_payments: int
    total_flights: int
    total_passengers: int

class AdminResetPasswordRequest(BaseModel):
    new_password: str

class AdminResetPasswordResponse(BaseModel):
    message: str

class BookingAdminFilter(BaseModel):
    user_id: Optional[int] = None
    flight_id: Optional[int] = None
    booking_status: Optional[str] = None
    payment_status: Optional[str] = None
    min_total_price: Optional[float] = None
    max_total_price: Optional[float] = None

class PaymentStatusUpdate(BaseModel):
    payment_status: PaymentStatus

class BookingStatusUpdate(BaseModel):
    booking_status: BookingStatus

class FlightAdminFilter(BaseModel):
    airline: Optional[str] = None
    origin: Optional[str] = None
    destination: Optional[str] = None
    status: Optional[FlightStatus] = None
    min_price: Optional[float] = None
    max_price: Optional[float] = None

class RecentActivity(BaseModel):
    recent_users: list[UserResponse]
    recent_bookings: list[BookingResponse]
    recent_flights: list[FlightResponse]

class AuditLogResponse(BaseModel):
    log_id: int
    admin_id: int
    action: str
    target_type: str
    target_id: int
    description: str
    timestamp: datetime

    class Config:
        from_attributes = True