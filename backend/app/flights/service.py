from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.flights.models import Flight
from app.flights import schemas


def create_flight(db: Session, flight: schemas.FlightCreate):
    db_flight = Flight(
        airline=flight.airline,
        origin=flight.origin,
        destination=flight.destination,
        departure_time=flight.departure_time,
        arrival_time=flight.arrival_time,
        price=flight.price,
        seats_available=flight.seats_available,
        status=flight.status
    )

    db.add(db_flight)
    db.commit()
    db.refresh(db_flight)

    return db_flight


def get_flights(db: Session):
    return db.query(Flight).all()


def get_flight(db: Session, flight_id: int):
    flight = db.query(Flight).filter(
        Flight.flight_id == flight_id
    ).first()

    if not flight:
        raise HTTPException(
            status_code=404,
            detail="Flight not found"
        )

    return flight

def search_flights(
    db: Session,
    origin: str | None = None,
    destination: str | None = None,
    airline: str | None = None,
    max_price: float | None = None
):
    query = db.query(Flight)

    if origin:
        query = query.filter(Flight.origin.ilike(f"%{origin}%"))

    if destination:
        query = query.filter(Flight.destination.ilike(f"%{destination}%"))

    if airline:
        query = query.filter(Flight.airline.ilike(f"%{airline}%"))

    if max_price:
        query = query.filter(Flight.price <= max_price)

    return query.all()