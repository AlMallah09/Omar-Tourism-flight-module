# Omar Tourism Flight Management System

## Project Overview

This project is a professional flight management and booking backend developed for Omar Tourism as part of an internship and system modernization initiative.

The system is being built using FastAPI and PostgreSQL to provide a scalable backend that can support future mobile applications, web integrations, and third-party flight providers.

The current implementation uses sample/mock data and is designed to be extended later with real flight provider APIs.

---

## Technology Stack

### Backend

* Python
* FastAPI
* SQLAlchemy
* PostgreSQL
* JWT Authentication
* Bcrypt Password Hashing

### Tools

* Swagger UI
* GitHub
* VS Code
* Postman

### Future Frontend

* Flutter Mobile Application
* Existing WordPress Traveler Website Integration

---

## Completed Phases

### Phase 1 – Project Planning and Architecture

* Requirements gathering
* System architecture design
* Technology stack selection
* Project documentation
* Development roadmap

### Phase 2 – Backend Foundation

* FastAPI setup
* PostgreSQL integration
* SQLAlchemy ORM
* Flight database model
* Flight CRUD endpoints
* Swagger testing

### Phase 3 – Booking Management

* User module
* Booking module
* Flight-booking relationships
* Seat availability management
* Booking creation
* Total price calculation
* Booking cancellation
* Seat restoration

### Phase 4 – Authentication and Authorization

* JWT authentication
* Password hashing with bcrypt
* Login endpoint
* Protected routes
* Current user extraction
* User-specific bookings
* Swagger authorization

### Phase 5 – Passenger Management

* Passenger database model
* Passenger APIs
* Passport information
* Nationality tracking
* Date of birth tracking
* Ticket number generation
* Passenger-booking relationships
* Booking details endpoint
* Ownership validation
* Cancelled booking protection

---

## Current Project Structure

```text
backend/
└── app/
    ├── authentication/
    ├── bookings/
    ├── flights/
    ├── passengers/
    ├── users/
    ├── db/
    ├── core/
    └── main.py
```

---

## Security Features

* JWT authentication
* Password hashing
* Protected endpoints
* Ownership validation
* Booking access restrictions
* Passenger access restrictions

---

## Current Status

Phase 5 Completed Successfully

Implemented Modules:

* Flights
* Users
* Authentication
* Bookings
* Passengers

---

## Next Phase

Phase 6 – Booking Enhancements and Reservation Workflow

Planned Features:

* Multi-passenger booking support
* Passenger validation improvements
* Reservation lifecycle management
* Advanced booking reporting
* Additional security controls

---

## Author

Ahmed Al Mallah

Computer Engineering Student

Omar Tourism Internship Project
