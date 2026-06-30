# Omar Tourism Flight Management System

A modern flight management backend built with **FastAPI** and **PostgreSQL**. The project is designed using a modular architecture that supports secure authentication, booking management, passenger management, and administrative operations while remaining scalable for future web and mobile integration.

---

## Current Version

**v0.6.3**

---

## Technology Stack

* Python
* FastAPI
* PostgreSQL
* SQLAlchemy
* Pydantic
* JWT Authentication
* Bcrypt Password Hashing

---

## Project Status

#### Completed

* ✅ Phase 1 – Project Planning and System Architecture
* ✅ Phase 2 – Backend Foundation and Flight Management
* ✅ Phase 3 – Booking Management System
* ✅ Phase 4 – Authentication and Authorization
* ✅ Phase 5 – Passenger Management System
* ✅ Phase 6.1 – Administration Foundation
* ✅ Phase 6.2 – Password and Account Security
* ✅ Phase 6.3 – Advanced Administration

---

## Current Development

**Phase 6.4 – Analytics & Business Intelligence**

Planned features include:

* Revenue analytics and reporting.
* Booking analytics and operational statistics.
* Flight performance analytics.
* Customer activity analytics.
* Destination and route analytics.
* Administrative dashboard KPIs.
* Business intelligence endpoints.
* Reporting enhancements.
* Additional production-readiness improvements.

---

## Current Features

#### Flight Management

* Flight CRUD operations
* Seat availability management
* Flight pricing
* Flight status management
* Soft flight cancellation
* Flight restoration
* Advanced flight filtering
* Public flight visibility control

#### Booking Management

* Flight reservations
* Automatic seat restoration
* Booking cancellation
* Booking ownership validation
* Booking status management
* Payment status management
* Advanced booking filtering
* Business rule validation

#### Passenger Management

* Passenger records
* Booking-to-passenger relationships
* Automatic ticket generation
* Passenger ownership validation

#### Authentication

* User registration
* Secure login
* JWT authentication
* Password hashing with bcrypt
* Protected API endpoints
* Change password
* Forgot password
* Password reset using secure tokens
* Password history
* Password reuse prevention
* Forced password change
* Account lockout
* Last login tracking

#### Administration

* Role-Based Access Control (RBAC)
* User management
* Booking management
* Flight management
* Administrative dashboard
* Dashboard statistics
* Payment management
* Booking status management
* Advanced booking filtering
* Advanced flight filtering
* Flight restoration
* Soft flight cancellation
* Audit logging
* Audit log retrieval
* Recent activity monitoring
* System health monitoring
* Pagination
* Enum validation
* Centralized status constants
* Response standardization
* Account enable and disable
* User search

---

## Project Structure

```text
app/
├── admin/
├── authentication/
├── bookings/
├── flights/
├── passengers/
├── users/
├── db/
└── core/
```

---

## Documentation

Project documentation is maintained in the `docs` directory and includes:

* Phase reports
* Development logs
* Architecture documentation
* Security documentation
* Roadmap
* Changelog

---

## Next Milestone

**Phase 6.4 – Analytics & Business Intelligence**

The next phase focuses on transforming operational data into business intelligence by introducing revenue analytics, booking statistics, customer insights, destination reporting, flight performance metrics, and dashboard KPIs to support administrative decision-making.