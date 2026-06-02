# Database Blueprint

## Purpose
This document defines the initial database blueprint for the Flight Booking System.

## Main Entities

### Users
Stores customer and admin account information.

Fields:
- user_id: Primary key
- name: User full name
- email: Unique user email
- password_hash: Encrypted password
- role: customer or admin
- created_at: Account creation date

### Flights
Stores flight information.

Fields:
- flight_id: Primary key
- flight_number: Unique flight identifier
- airline_name: Airline company name
- origin: Departure city/airport
- destination: Arrival city/airport
- departure_time: Flight departure date and time
- arrival_time: Flight arrival date and time
- price: Flight ticket price
- total_seats: Total number of seats
- available_seats: Number of available seats
- status: active, delayed, cancelled

### Bookings
Stores customer flight bookings.

Fields:
- booking_id: Primary key
- user_id: Foreign key referencing Users
- flight_id: Foreign key referencing Flights
- booking_date: Date of booking
- status: confirmed, cancelled, pending
- total_price: Final booking price

### Payments
Stores payment records.

Fields:
- payment_id: Primary key
- booking_id: Foreign key referencing Bookings
- payment_method: card, cash, online
- payment_status: paid, unpaid, refunded
- amount: Payment amount
- payment_date: Date of payment

### Audit Logs
Stores important system actions.

Fields:
- log_id: Primary key
- user_id: Foreign key referencing Users
- action: Description of action performed
- table_affected: Table that was modified
- created_at: Time of action

## Relationships

- One user can create many bookings.
- One flight can have many bookings.
- One booking can have one payment.
- One user can create many audit log records.

## Data Integrity Rules

1. Email must be unique.
2. Flight number must be unique.
3. Available seats cannot be less than zero.
4. Booking must belong to an existing user.
5. Booking must belong to an existing flight.
6. Payment must belong to an existing booking.
7. Admin actions should be recorded in audit logs.

## Seat Management Logic

When a booking is confirmed:
1. System checks if available_seats is greater than zero.
2. If seats are available, booking is created.
3. available_seats decreases by 1.
4. If no seats are available, booking is rejected.

When a booking is cancelled:
1. Booking status changes to cancelled.
2. available_seats increases by 1.
3. Cancellation is recorded in audit logs.