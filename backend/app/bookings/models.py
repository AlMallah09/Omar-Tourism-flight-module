from sqlalchemy import Column, Integer, Float, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.db.base import Base


class Booking(Base):
    __tablename__ = "bookings"

    booking_id = Column(Integer, primary_key=True, index=True)

    user_id = Column(Integer, ForeignKey("users.user_id"), nullable=False)
    flight_id = Column(Integer, ForeignKey("flights.flight_id"), nullable=False)

    booking_date = Column(DateTime(timezone=True), server_default=func.now())
    number_of_passengers = Column(Integer, nullable=False)
    total_price = Column(Float, nullable=False)
    booking_status = Column(String, default="confirmed")

    user = relationship("User", back_populates="bookings")
    flight = relationship("Flight", back_populates="bookings")
    passengers = relationship("Passenger", back_populates="booking")