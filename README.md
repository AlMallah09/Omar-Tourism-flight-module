# Omar Tourism Flight Management System

A modern flight management backend built with **FastAPI** and **PostgreSQL**. The project is designed using a modular architecture that supports secure authentication, booking management, passenger management, and administrative operations while remaining scalable for future web and mobile integration.

---

## Current Version

**v0.6.2**

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

### Completed

* ✅ Phase 1 — Project Planning and System Architecture
* ✅ Phase 2 — Backend Foundation and Flight Management
* ✅ Phase 3 — Booking Management System
* ✅ Phase 4 — Authentication and Authorization
* ✅ Phase 5 — Passenger Management System
* ✅ Phase 6.1 — Administration Foundation
* ✅ Phase 6.2 — Password and Account Security

### Current Development

**Phase 6.3 — Advanced Administration**

Planned features include:

* Pagination across administrative endpoints.
* Sorting support for users, bookings, flights, and passengers.
* Advanced user search and filtering.
* Advanced booking search and filtering.
* Flight search and filtering enhancements.
* Passenger search and filtering.
* Passenger manifest generation.
* Dashboard enhancements with richer administrative insights.
* Service-layer refactoring where appropriate.
* Additional administrative quality-of-life improvements.


---

## Current Features

### Flight Management

* Flight CRUD operations
* Seat availability management
* Flight pricing
* Flight status management

### Booking Management

* Flight reservations
* Automatic seat allocation
* Automatic seat restoration
* Booking cancellation
* Booking ownership validation

### Passenger Management

* Passenger records
* Booking-to-passenger relationships
* Automatic ticket generation
* Passenger ownership validation

### Authentication

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

### Administration

* Role-Based Access Control (RBAC)
* User management
* Booking management
* Administrative dashboard
* Dashboard statistics
* Audit logging
* Soft delete
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

**Phase 6.2 — Password and Security**

The next phase focuses on strengthening account security through password management, account recovery, login protection, and additional security controls while continuing to improve the administration platform.
