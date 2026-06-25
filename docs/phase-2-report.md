# Phase 2 Report

## Phase Title

Backend Foundation and Flight Management Module

---

## Objective

Build the core backend infrastructure by configuring the development environment, integrating the database, implementing the Flight module, and exposing the first REST API endpoints.

---

## Implementation

The backend foundation was established by configuring the FastAPI application, connecting it to a PostgreSQL database, and organizing the project into a modular structure that supports future expansion. SQLAlchemy was integrated as the ORM to simplify database operations while keeping the data layer maintainable.

The Flight module was implemented as the first business component of the system. A relational database model was created to store flight information, including airline details, departure and arrival locations, schedules, pricing, seat availability, and operational status. Data validation was introduced through Pydantic schemas to ensure consistent request and response handling.

A dedicated service layer was added to separate business logic from API routes, making the application easier to maintain as new features are introduced. CRUD endpoints were then implemented to allow flights to be created, retrieved, updated, and removed through REST APIs.

Throughout development, each endpoint was verified using the automatically generated Swagger documentation. Database operations were validated to ensure records were stored, updated, and retrieved correctly without affecting data integrity.

---

## Deliverables

* FastAPI backend configuration.
* PostgreSQL database integration.
* SQLAlchemy ORM configuration.
* Flight database model.
* Flight database table.
* Flight request and response schemas.
* Flight service layer.
* Flight CRUD REST APIs.
* Swagger API documentation.
* Verified database persistence.

---

## Testing

The backend was tested using Swagger UI to verify all CRUD operations. Database records were validated after each operation to confirm successful persistence. Input validation was also tested to ensure invalid requests were rejected while valid requests produced the expected responses.

---

## Outcome

Phase 2 transformed the project from a planned architecture into a functional backend application. The database integration, Flight module, and REST APIs established the first working component of the system and created the foundation required for the remaining business modules.
