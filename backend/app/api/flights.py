from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.database import SessionLocal
from app.schemas.flight import FlightCreate, FlightResponse
from app.services.flight_service import create_flight


router = APIRouter(
    prefix="/flights",
    tags=["Flights"]
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=FlightResponse)
def add_flight(
    flight_data: FlightCreate,
    db: Session = Depends(get_db)
):
    return create_flight(db, flight_data)