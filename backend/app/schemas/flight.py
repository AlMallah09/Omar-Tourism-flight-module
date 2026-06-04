from pydantic import BaseModel


class FlightBase(BaseModel):
    airline: str
    flight_number: str
    origin: str
    destination: str


class FlightCreate(FlightBase):
    pass


class FlightResponse(FlightBase):
    id: int

    class Config:
        from_attributes = True