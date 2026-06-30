from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.flights.models import Flight
from app.flights import schemas, models
from app.admin.schemas import FlightAdminFilter
from app.core.constants import FlightStatus

def get_flights(db: Session):
    return (
    db.query(Flight)
    .filter(Flight.status != FlightStatus.CANCELLED)
    .all()
)

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

def get_all_flights_admin(db: Session, page: int = 1, page_size: int = 20):
    if page < 1:
        page = 1

    if page_size < 1:
        page_size = 20

    if page_size > 100:
        page_size = 100

    offset = (page - 1) * page_size

    return (
        db.query(models.Flight)
        .order_by(models.Flight.flight_id.desc())
        .offset(offset)
        .limit(page_size)
        .all()
    )

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

def filter_flights_admin(
    db: Session,
    filters: FlightAdminFilter,
    page: int = 1,
    page_size: int = 20
):
    query = db.query(models.Flight)

    if filters.airline:
        airline_exists = db.query(models.Flight).filter(
            models.Flight.airline.ilike(f"%{filters.airline}%")
        ).first()

        if not airline_exists:
            raise HTTPException(
                status_code=404,
                detail=f"Airline '{filters.airline}' does not exist."
            )

        query = query.filter(
            models.Flight.airline.ilike(f"%{filters.airline}%")
        )

    if filters.origin:
        origin_exists = db.query(models.Flight).filter(
            models.Flight.origin.ilike(f"%{filters.origin}%")
        ).first()

        if not origin_exists:
            raise HTTPException(
                status_code=404,
                detail=f"Origin '{filters.origin}' does not exist."
            )

        query = query.filter(
            models.Flight.origin.ilike(f"%{filters.origin}%")
        )

    if filters.destination:
        destination_exists = db.query(models.Flight).filter(
            models.Flight.destination.ilike(f"%{filters.destination}%")
        ).first()

        if not destination_exists:
            raise HTTPException(
                status_code=404,
                detail=f"Destination '{filters.destination}' does not exist."
            )

        query = query.filter(
            models.Flight.destination.ilike(f"%{filters.destination}%")
        )

    if filters.status:
        status_exists = db.query(models.Flight).filter(
            models.Flight.status.ilike(filters.status)
        ).first()

        if not status_exists:
            raise HTTPException(
                status_code=404,
                detail=f"Status '{filters.status}' does not exist."
            )

        query = query.filter(
            models.Flight.status.ilike(filters.status)
        )

    if filters.min_price is not None:
        query = query.filter(models.Flight.price >= filters.min_price)

    if filters.max_price is not None:
        query = query.filter(models.Flight.price <= filters.max_price)

    if page < 1:
       page = 1

    if page_size < 1:
       page_size = 20

    if page_size > 100:
       page_size = 100

    offset = (page - 1) * page_size

    results = (
        query.order_by(models.Flight.flight_id.desc())
        .offset(offset)
        .limit(page_size)
        .all()
)

    if not results:
        raise HTTPException(
            status_code=404,
            detail="No flights found matching the specified filters."
    )

    return results

def update_flight(
    db: Session,
    flight_id: int,
    flight_update: schemas.FlightUpdate
):
    flight = db.query(models.Flight).filter(
        models.Flight.flight_id == flight_id
    ).first()

    if not flight:
        raise HTTPException(
            status_code=404,
            detail="Flight not found"
        )

    update_data = flight_update.model_dump(exclude_unset=True)

    for key, value in update_data.items():
        setattr(flight, key, value)

    db.commit()
    db.refresh(flight)

    return flight

def delete_flight(
    db: Session,
    flight_id: int
):
    flight = db.query(models.Flight).filter(
        models.Flight.flight_id == flight_id
    ).first()

    if not flight:
        raise HTTPException(
            status_code=404,
            detail="Flight not found"
        )

    flight.status = FlightStatus.CANCELLED

    db.commit()
    db.refresh(flight)

    return flight

def restore_flight(
    db: Session,
    flight_id: int
):
    flight = db.query(models.Flight).filter(
        models.Flight.flight_id == flight_id
    ).first()

    if not flight:
        raise HTTPException(
            status_code=404,
            detail="Flight not found"
        )

    if flight.status.lower() != FlightStatus.CANCELLED.lower():
        raise HTTPException(
            status_code=400,
            detail="Flight is not cancelled."
        )

    flight.status = FlightStatus.SCHEDULED

    db.commit()
    db.refresh(flight)

    return flight