# Database Analysis and Design

## Purpose

This document defines the preliminary database structure for the flight management and booking backend.

The first version will use mock/sample flight data stored in PostgreSQL.

## Main Tables

### Users

Stores customer and admin account information.

Fields:
- user_id
- full_name
- email
- password_hash
- role
- created_at

### Flights

Stores sample flight data.

Fields:
- flight_id
- flight_number
- airline_name
- origin
- destination
- departure_time
- arrival_time
- price
- total_seats
- available_seats
- status

### Bookings

Stores user booking records.

Fields:
- booking_id
- user_id
- flight_id
- booking_date
- booking_status
- total_price

### Payments

Stores payment-related information.

Fields:
- payment_id
- booking_id
- payment_method
- payment_status
- amount
- payment_date

### Audit Logs

Stores important system actions.

Fields:
- log_id
- user_id
- action
- table_affected
- created_at

## Relationships

- One user can have many bookings.
- One flight can have many bookings.
- One booking can have one payment.
- One user can have many audit log records.

## Data Integrity Rules

- User email must be unique.
- Flight number must be unique.
- Available seats cannot be less than zero.
- A booking must belong to an existing user.
- A booking must belong to an existing flight.
- A payment must belong to an existing booking.