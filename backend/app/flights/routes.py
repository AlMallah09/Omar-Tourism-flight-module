from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.flights import schemas, service


router = APIRouter(
    prefix="/flights",
    tags=["Flights"]
)


@router.post("/", response_model=schemas.FlightResponse)
def create_flight(flight: schemas.FlightCreate, db: Session = Depends(get_db)):
    return service.create_flight(db, flight)


@router.get("/", response_model=list[schemas.FlightResponse])
def get_flights(db: Session = Depends(get_db)):
    return service.get_flights(db)


@router.get("/{flight_id}", response_model=schemas.FlightResponse)
def get_flight(flight_id: int, db: Session = Depends(get_db)):
    return service.get_flight(db, flight_id)

@router.get("/search/")
def search_flights(
    origin: str | None = None,
    destination: str | None = None,
    airline: str | None = None,
    max_price: float | None = None,
    db: Session = Depends(get_db)
):
    return service.search_flights(
        db,
        origin,
        destination,
        airline,
        max_price
    )