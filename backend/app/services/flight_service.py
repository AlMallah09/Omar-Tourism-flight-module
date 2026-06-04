from sqlalchemy.orm import Session

from app.models.flight import Flight
from app.schemas.flight import FlightCreate


def create_flight(db: Session, flight_data: FlightCreate):
    flight = Flight(**flight_data.model_dump())

    db.add(flight)
    db.commit()
    db.refresh(flight)

    return flight