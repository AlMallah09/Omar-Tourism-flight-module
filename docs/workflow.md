# Flight Booking Workflow

## Customer Workflow

1. Customer opens the website or mobile application.
2. Customer searches for flights.
3. Backend returns available mock/sample flights.
4. Customer selects a flight.
5. Customer logs in or registers.
6. Customer creates a booking.
7. Backend stores the booking in PostgreSQL.
8. Backend updates available seat count.
9. Customer receives booking confirmation.

## Admin Workflow

1. Admin logs in.
2. Admin adds or updates flight records.
3. Admin manages flight availability.
4. Admin views customer bookings.
5. Admin monitors booking activity.

## Future Provider Workflow

1. Customer searches for a flight.
2. Backend sends request to third-party provider API.
3. Provider returns real availability and pricing.
4. Customer selects flight.
5. Backend confirms booking through provider API.
6. Booking is saved in local database.