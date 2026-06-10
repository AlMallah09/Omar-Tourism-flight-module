from app.db.base import Base
from app.db.database import engine

from app.flights.models import Flight
from app.users.models import User
from app.bookings.models import Booking
from app.passengers import models as passenger_models


Base.metadata.create_all(bind=engine)

print("Tables created successfully.")