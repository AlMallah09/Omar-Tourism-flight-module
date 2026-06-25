# Phase 5 Report

## Phase Title

Passenger Management System

---

## Objective

Extend the booking system by introducing passenger management, allowing each reservation to store passenger information while maintaining secure ownership validation and preserving booking integrity throughout the reservation process.

---

## Implementation

The Passenger module was introduced to manage traveler information associated with individual bookings. A dedicated passenger model was created and linked directly to the Booking module, allowing multiple passengers to be assigned to a single reservation while maintaining a clear relationship between bookings and traveler records.

Passenger information was structured to include personal details required during the booking process, such as full name, date of birth, nationality, passport number, and automatically generated ticket numbers. Validation was applied through Pydantic schemas to ensure data consistency before records were stored in the database.

The booking workflow was extended to support passenger management without affecting existing reservation logic. Ownership validation was applied to every passenger-related operation, ensuring users could only create or view passengers belonging to bookings they owned.

Additional business rules were introduced to protect data integrity. Passengers cannot be added to cancelled bookings, preventing inconsistencies between booking status and passenger records. A dedicated endpoint was also implemented to retrieve all passengers associated with a specific booking, providing a complete view of the reservation.

Finally, the booking details endpoint was enhanced to include passenger information, allowing a single request to return the reservation together with every traveler assigned to it.

---

## Deliverables

* Passenger database model.
* Passenger database table.
* Booking-to-Passenger relationship.
* Passenger request and response schemas.
* Passenger service layer.
* Passenger management API endpoints.
* Automatic ticket number generation.
* Ownership validation for passenger operations.
* Protection against adding passengers to cancelled bookings.
* Booking details endpoint with passenger information.

---

## Testing

Passenger creation, retrieval, and ownership validation were verified using Swagger UI. Multiple booking scenarios were tested to confirm that passengers could only be managed by the booking owner. Business rules preventing passenger creation for cancelled bookings were also validated, together with automatic ticket number generation and booking detail retrieval.

---

## Outcome

Phase 5 expanded the reservation workflow by introducing complete passenger management. Bookings now support multiple passengers while enforcing ownership validation and business rules that preserve data integrity. The system is now capable of managing reservations at a level much closer to a real-world airline booking platform.
