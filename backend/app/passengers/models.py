from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship

from app.db.base import Base


class Passenger(Base):
    __tablename__ = "passengers"

    passenger_id = Column(Integer, primary_key=True, index=True)

    booking_id = Column(
        Integer,
        ForeignKey("bookings.booking_id"),
        nullable=False
    )

    first_name = Column(String, nullable=False)

    last_name = Column(String, nullable=False)

    passport_number = Column(
        String,
        unique=True,
        nullable=False
    )

    nationality = Column(
        String,
        nullable=False
    )

    date_of_birth = Column(
        Date,
        nullable=False
    )

    ticket_number = Column(
        String,
        unique=True,
        nullable=False
    )

    booking = relationship(
        "Booking",
        back_populates="passengers"
    )