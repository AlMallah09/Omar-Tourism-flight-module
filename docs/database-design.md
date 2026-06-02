# Database Design

## USERS

Fields:

* user_id
* name
* email
* password_hash
* role
* created_at

## FLIGHTS

Fields:

* flight_id
* flight_number
* origin
* destination
* departure_time
* arrival_time
* price
* total_seats
* available_seats

## BOOKINGS

Fields:

* booking_id
* user_id
* flight_id
* booking_date
* status

## Relationships

* One User can have multiple Bookings.
* One Flight can have multiple Bookings.
* Each Booking belongs to one User and one Flight.
