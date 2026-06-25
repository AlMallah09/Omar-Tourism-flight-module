# Development Log – Phase 5

## Phase Title

Passenger Management System

---

## Objective

Introduce passenger management into the reservation workflow and establish the relationship between bookings and travelers while maintaining security, ownership validation, and booking consistency.

---

## Activities Completed

* Implemented the Passenger database model.
* Created the Passengers database table.
* Established the Booking-to-Passenger relationship.
* Developed passenger request and response schemas.
* Implemented the Passenger service layer.
* Developed passenger management API endpoints.
* Implemented automatic ticket number generation.
* Added ownership validation for passenger operations.
* Prevented passenger creation for cancelled bookings.
* Implemented endpoint to retrieve passengers by booking.
* Enhanced booking details endpoint to include passenger information.
* Verified passenger workflows using Swagger UI.

---

## Challenges Encountered

The passenger module introduced another level of relationships within the system. It was important to ensure passenger records always remained synchronized with their associated bookings while preserving existing business rules and authorization logic.

---

## Solutions Applied

Passenger operations were integrated directly into the booking workflow through controlled service-layer logic. Ownership validation was reused from the existing authentication system, while additional business rules prevented invalid operations such as adding passengers to cancelled bookings.

---

## Technical Decisions

* Linked passengers directly to bookings through relational database models.
* Generated ticket numbers automatically during passenger creation.
* Reused existing authorization mechanisms for ownership validation.
* Extended booking responses to include passenger information.
* Continued following the modular architecture by separating routes, services, models, and schemas.

---

## Outcome

The reservation workflow now supports complete passenger management without compromising the integrity of existing booking operations. The backend evolved from handling reservations alone to managing both reservations and the travelers associated with them, creating a more complete and practical flight management system.

---

## Next Phase

Expand the platform with an administration and security layer by introducing role-based access control, administrative tools, dashboard analytics, audit logging, and advanced account management features.
