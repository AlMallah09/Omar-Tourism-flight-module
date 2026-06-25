# Phase 3 Report

## Phase Title

Booking Management System

---

## Objective

Implement a complete booking management system by introducing user-booking relationships, flight-booking relationships, booking lifecycle management, automatic seat allocation, and pricing logic.

---

## Implementation

The Booking module was developed to handle the complete reservation workflow within the system. A dedicated booking model was introduced and linked to both users and flights, allowing each reservation to maintain clear ownership while preserving the relationship between passengers and their selected flights.

Business rules were implemented to validate seat availability before a booking could be confirmed. When a reservation is successfully created, the available seat count is automatically reduced to prevent overbooking. The total booking price is calculated dynamically using the selected flight information, ensuring pricing remains consistent with the latest flight data.

Support for booking cancellation was also introduced. Rather than removing booking records from the database, cancellations update the booking status while automatically restoring the reserved seat back to the flight. This preserves booking history and maintains accurate seat availability without compromising data integrity.

The entire booking workflow was integrated with the existing Flight module, creating the first complete business process within the system.

---

## Deliverables

* Booking database model.
* User and Booking relationship.
* Flight and Booking relationship.
* Booking request and response schemas.
* Booking service layer.
* Booking CRUD APIs.
* Automatic seat availability validation.
* Dynamic booking price calculation.
* Booking cancellation workflow.
* Automatic seat restoration.

---

## Testing

The booking workflow was validated using Swagger UI. Booking creation, retrieval, cancellation, and seat restoration were tested with multiple scenarios to verify business rules. Edge cases such as unavailable seats and repeated cancellations were also verified to ensure the system handled invalid operations correctly.

---

## Outcome

Phase 3 introduced the project's first complete business workflow. Users can now reserve flights, pricing is calculated automatically, seat availability is managed in real time, and booking history is preserved through controlled cancellation rather than data deletion.
