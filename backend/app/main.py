from fastapi import FastAPI

from app.api.flights import router as flights_router


app = FastAPI(
    title="Omar Tourism Flight API"
)


app.include_router(flights_router)


@app.get("/")
def root():
    return {"message": "Omar Tourism Flight API is running"}