from fastapi import FastAPI

from app.flights.routes import router as flights_router
from app.users.routes import router as users_router
from app.bookings.routes import router as bookings_router
from app.authentication.routes import router as authentication_router
from app.passengers import models as passenger_models
from app.passengers.routes import router as passengers_router

app = FastAPI(
    title="Omar Tourism Flight Module API",
    version="1.0.0"
)


app.include_router(flights_router)
app.include_router(users_router)
app.include_router(bookings_router)
app.include_router(authentication_router)
app.include_router(passengers_router)


@app.get("/")
def root():
    return {"message": "Omar Tourism API is running"}