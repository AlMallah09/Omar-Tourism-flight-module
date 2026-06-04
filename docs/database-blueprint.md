# Database Blueprint

## Purpose

This document defines the proposed PostgreSQL database blueprint for the Python FastAPI backend.

The first version will use mock/sample flight data. Future versions may connect to official third-party flight or hotel provider APIs.

## Main Entities

### Users

Stores customer and admin account information.

Fields:

* user_id
* full_name
* email
* password_hash
* role
* created_at

### Flights

Stores mock/sample flight records.

Fields:

* flight_id
* flight_number
* airline_name
* origin
* destination
* departure_time
* arrival_time
* price
* total_seats
* available_seats
* status

### Bookings

Stores customer booking records.

Fields:

* booking_id
* user_id
* flight_id
* booking_date
* booking_status
* total_price

### Payments

Stores payment-related records for future use.

Fields:

* payment_id
* booking_id
* payment_method
* payment_status
* amount
* payment_date

### Audit Logs

Stores important system actions.

Fields:

* log_id
* user_id
* action
* table_affected
* created_at

## Relationships

* One user can have many bookings.
* One flight can have many bookings.
* One booking can have one payment.
* One user can have many audit log records.

## Data Integrity Rules

1. Email must be unique.
2. Flight number must be unique.
3. Available seats cannot be less than zero.
4. A booking must belong to an existing user.
5. A booking must belong to an existing flight.
6. A payment must belong to an existing booking.
7. Important admin actions should be recorded in audit logs.
