from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional


class FlightBase(BaseModel):
    airline: str
    origin: str
    destination: str
    departure_time: datetime
    arrival_time: datetime
    price: float
    status: str


class FlightCreate(FlightBase):
    total_seats: int = Field(gt=0)


class FlightResponse(FlightBase):
    flight_id: int
    total_seats: int
    seats_available: int

    class Config:
        from_attributes = True

class FlightUpdate(BaseModel):
    airline: Optional[str] = None
    origin: Optional[str] = None
    destination: Optional[str] = None
    departure_time: Optional[datetime] = None
    arrival_time: Optional[datetime] = None
    price: Optional[float] = None
    total_seats: Optional[int] = Field(default=None, gt=0)
    status: Optional[str] = None