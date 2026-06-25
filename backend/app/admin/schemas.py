from pydantic import BaseModel

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

    total_flights: int
    total_passengers: int

class AdminResetPasswordRequest(BaseModel):
    new_password: str


class AdminResetPasswordResponse(BaseModel):
    message: str