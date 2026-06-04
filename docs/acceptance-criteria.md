# Acceptance Criteria

## Backend Foundation

The backend foundation is complete when:
- FastAPI runs successfully.
- The root endpoint returns a valid JSON response.
- Automatic API documentation is available.
- The backend structure is organized and scalable.

## Database

The database phase is complete when:
- PostgreSQL is connected.
- Required tables are created.
- Relationships are defined.
- Mock flight data can be stored and retrieved.

## Authentication

Authentication is complete when:
- Users can register.
- Users can log in.
- Passwords are hashed.
- JWT tokens are generated.
- Protected routes reject unauthorized access.

## Flight Module

The flight module is complete when:
- Flights can be created.
- Flights can be searched.
- Flight details can be viewed.
- Admins can update and delete flights.

## Booking Module

The booking module is complete when:
- Users can create bookings.
- Seat availability updates after booking.
- Users can view bookings.
- Users can cancel bookings.

## Integration Readiness

The system is integration-ready when:
- APIs are documented.
- Mock data can later be replaced by provider API data.
- The backend can serve both web and mobile clients.