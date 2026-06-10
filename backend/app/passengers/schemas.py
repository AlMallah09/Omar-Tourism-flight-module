from datetime import date
from pydantic import BaseModel


class PassengerCreate(BaseModel):
    first_name: str
    last_name: str
    passport_number: str
    nationality: str
    date_of_birth: date


class PassengerResponse(BaseModel):
    passenger_id: int
    booking_id: int
    first_name: str
    last_name: str
    passport_number: str
    nationality: str
    date_of_birth: date
    ticket_number: str

    class Config:
        from_attributes = True