import uuid
from sqlalchemy.orm import Session

from app.passengers.models import Passenger
from app.passengers.schemas import PassengerCreate


def generate_ticket_number():
    return "TKT-" + str(uuid.uuid4())[:8].upper()


def create_passenger(
    db: Session,
    booking_id: int,
    passenger_data: PassengerCreate
):
    passenger = Passenger(
        booking_id=booking_id,
        first_name=passenger_data.first_name,
        last_name=passenger_data.last_name,
        passport_number=passenger_data.passport_number,
        nationality=passenger_data.nationality,
        date_of_birth=passenger_data.date_of_birth,
        ticket_number=generate_ticket_number()
    )

    db.add(passenger)
    db.commit()
    db.refresh(passenger)

    return passenger

def get_passengers_by_booking(
    db: Session,
    booking_id: int
):
    return db.query(Passenger).filter(
        Passenger.booking_id == booking_id
    ).all()