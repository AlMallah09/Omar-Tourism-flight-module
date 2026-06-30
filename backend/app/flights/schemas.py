from pydantic import BaseModel
from datetime import datetime
from typing import Optional


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

class FlightUpdate(BaseModel):
    airline: Optional[str] = None
    origin: Optional[str] = None
    destination: Optional[str] = None
    departure_time: Optional[datetime] = None
    arrival_time: Optional[datetime] = None
    price: Optional[float] = None
    seats_available: Optional[int] = None
    status: Optional[str] = None