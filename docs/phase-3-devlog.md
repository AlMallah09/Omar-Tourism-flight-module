# Development Log – Phase 3

## Phase Title

Booking Management System

---

## Objective

Develop the booking workflow by connecting users and flights through reservations while enforcing business rules for pricing, seat availability, and booking management.

---

## Activities Completed

* Implemented the Booking database model.
* Created the Bookings database table.
* Established User-to-Booking relationship.
* Established Flight-to-Booking relationship.
* Developed booking request and response schemas.
* Implemented the Booking service layer.
* Developed booking API endpoints.
* Added automatic booking price calculation.
* Added seat availability validation.
* Implemented automatic seat deduction after successful booking.
* Implemented booking cancellation.
* Implemented automatic seat restoration after cancellation.
* Verified the complete booking workflow using Swagger UI.

---

## Challenges Encountered

The booking process required multiple database updates to occur as a single business operation. Seat availability, booking creation, and pricing all needed to remain synchronized to prevent inconsistent data.

---

## Solutions Applied

Business logic was centralized within the service layer to ensure every booking operation followed the same sequence of validations and database updates. Automatic seat management was integrated directly into the booking workflow to eliminate manual intervention and reduce the risk of inconsistent records.

---

## Technical Decisions

* Connected bookings to both users and flights through relational models.
* Managed seat availability automatically within booking operations.
* Calculated booking prices dynamically using flight data.
* Preserved booking history by using status-based cancellation instead of deleting records.
* Continued separating API routes from business logic to improve maintainability.

---

## Outcome

The project evolved from managing individual flights to supporting complete reservations. The backend now enforces booking rules, maintains data consistency across related entities, and provides a reliable reservation workflow for future expansion.

---

## Next Phase

Implement authentication and authorization by introducing user registration, secure login, JWT-based authentication, protected endpoints, and user-specific booking management.
