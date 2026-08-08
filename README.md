# Omar Tourism Flight Management System

A modern flight management backend built with **FastAPI** and **PostgreSQL**. The project is designed using a modular architecture that supports secure authentication, booking management, passenger management, and administrative operations while remaining scalable for future web and mobile integration.

---

## Current Version

**v0.6.4**

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
* ✅ Phase 6.4 – Analytics and Business Intelligence

---

## Current Development

### Current Development

**Phase 6.5 – Reports and Exports**

Planned features include:

* Administrative report generation.
* Booking reports.
* Flight reports.
* Customer reports.
* Revenue reports.
* Analytics-based business reports.
* CSV export support.
* Structured downloadable datasets.
* Date-range filtering for reports.
* Reusable reporting service architecture.
* Administrator-only report and export access.

---

## Current Features

#### Flight Management

* Flight CRUD operations
* Total flight capacity management
* Automatic seat availability initialization
* Seat availability management
* Safe flight capacity updates
* Flight pricing
* Flight status management
* Soft flight cancellation and restoration
* Advanced flight filtering

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

#### Analytics and Business Intelligence

* Revenue analytics
* Booking analytics
* Flight analytics
* Customer analytics
* Customer growth tracking
* Destination analytics
* Origin analytics
* Route performance analytics
* Monthly booking and revenue trends
* Flight performance analytics
* Flights-without-bookings analysis
* Flight occupancy and seat utilization
* Consolidated analytics dashboard
* Key Performance Indicator (KPI) analytics
* Administrator-protected analytics endpoints

---

## Project Structure

```text
app/
├── admin/
├── analytics/
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

## Next Milestone

**Phase 6.5 – Reports and Exports**

The next phase will introduce structured reporting and data export capabilities built on top of the existing administration and analytics layers. Operational and analytical information will be made available through reusable reporting services and downloadable formats for business use, record keeping, and external analysis.