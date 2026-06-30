from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.flights import schemas
from app.flights import services
from app.users.models import User
from app.authentication.utils import admin_required
from app.admin.schemas import FlightAdminFilter


router = APIRouter(
    prefix="/flights",
    tags=["Flights"]
)


@router.get("/", response_model=list[schemas.FlightResponse], tags=["Flights - Public"])
def get_flights(db: Session = Depends(get_db)):
    return services.get_flights(db)

@router.get("/search/", tags=["Flights - Public"])
def search_flights(
    origin: str | None = None,
    destination: str | None = None,
    airline: str | None = None,
    max_price: float | None = None,
    db: Session = Depends(get_db)
):
    return services.search_flights(
        db,
        origin,
        destination,
        airline,
        max_price
    )

@router.get("/{flight_id}", response_model=schemas.FlightResponse, tags=["Flights - Admin"])
def get_flight(flight_id: int, db: Session = Depends(get_db)):
    return services.get_flight(db, flight_id)

@router.get("/admin/all", response_model=list[schemas.FlightResponse], tags=["Flights - Admin"])
def get_all_flights_admin(
    page: int = 1,
    page_size: int = 20,
    db: Session = Depends(get_db),
    current_admin: User = Depends(admin_required)
):
    return services.get_all_flights_admin(db, page, page_size)

@router.post("/admin/filter", response_model=list[schemas.FlightResponse])
def filter_flights_admin(
    filters: FlightAdminFilter,
    page: int = 1,
    page_size: int = 20,
    db: Session = Depends(get_db),
    current_admin: User = Depends(admin_required)
):
    return services.filter_flights_admin(db, filters, page, page_size)

@router.post("/", response_model=schemas.FlightResponse, tags=["Flights - Admin Management"])
def create_flight(
    flight: schemas.FlightCreate,
    db: Session = Depends(get_db),
    current_admin: User = Depends(admin_required)
):
    return services.create_flight(db, flight)

@router.put("/{flight_id}", response_model=schemas.FlightResponse, tags=["Flights - Admin Management"])
def update_flight(
    flight_id: int,
    flight: schemas.FlightUpdate,
    db: Session = Depends(get_db),
    current_admin: User = Depends(admin_required)
):
    if flight.status.lower() == "cancelled":
        raise HTTPException(status_code=404, detail="Flight not found")
    return services.update_flight(db, flight_id, flight)

@router.put("/{flight_id}/restore", response_model=schemas.FlightResponse, tags=["Flights - Admin Management"])
def restore_flight(
    flight_id: int,
    db: Session = Depends(get_db),
    current_admin: User = Depends(admin_required)
):
    return services.restore_flight(db, flight_id)

@router.delete("/{flight_id}", response_model=schemas.FlightResponse, tags=["Flights - Admin Management"])
def delete_flight(
    flight_id: int,
    db: Session = Depends(get_db),
    current_admin: User = Depends(admin_required)
):
    return services.delete_flight(db, flight_id)

