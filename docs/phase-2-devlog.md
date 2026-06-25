# Development Log – Phase 2

## Phase Title

Backend Foundation and Flight Management Module

---

## Objective

Establish the backend infrastructure and implement the first functional module responsible for managing flight information.

---

## Activities Completed

* Configured the FastAPI development environment.
* Connected the application to PostgreSQL.
* Configured SQLAlchemy ORM.
* Organized the backend project structure.
* Implemented the Flight database model.
* Created the Flights database table.
* Developed request and response schemas using Pydantic.
* Implemented the Flight service layer.
* Developed CRUD API endpoints for flights.
* Integrated Swagger documentation.
* Verified database persistence through API testing.

---

## Challenges Encountered

Designing the project structure required careful planning to ensure future modules could be integrated without introducing unnecessary dependencies. Establishing a clear separation between routes, services, models, and schemas was also important for long-term maintainability.

---

## Solutions Applied

A modular architecture was adopted, separating database models, API routes, business logic, and validation schemas into dedicated components. This structure simplifies future development and encourages code reuse across the application.

---

## Technical Decisions

* Adopted SQLAlchemy as the ORM layer.
* Introduced Pydantic for request and response validation.
* Separated business logic into service classes.
* Implemented RESTful API design principles.
* Used Swagger UI for endpoint verification during development.

---

## Outcome

The backend infrastructure became fully operational with a functioning Flight module and reliable database connectivity. The project was now capable of managing flight data through REST APIs and provided a stable platform for implementing user accounts and booking functionality.

---

## Next Phase

Implement the booking system by introducing user accounts, booking management, entity relationships, seat availability management, dynamic pricing, and booking lifecycle operations.
