from pydantic import BaseModel
from datetime import datetime


class FlightBase(BaseModel):
    airline: str
    origin: str
    destination: str
    departure_time: datetime
    arrival_time: datetime
    price: float
    seats_available: int
    status: str


class FlightCreate(FlightBase):
    pass


class FlightResponse(FlightBase):
    flight_id: int

    class Config:
        from_attributes = True