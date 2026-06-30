from pydantic import BaseModel
from datetime import datetime
from app.passengers.schemas import PassengerResponse


class BookingBase(BaseModel):
    flight_id: int
    number_of_passengers: int


class BookingCreate(BookingBase):
    pass


class BookingResponse(BookingBase):
    booking_id: int
    user_id: int
    booking_date: datetime
    total_price: float
    booking_status: str
    payment_status: str

    class Config:
        from_attributes = True

class BookingDetailsResponse(BookingResponse):
    passengers: list[PassengerResponse]
        