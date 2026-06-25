# Phase 4 Report

## Phase Title

Authentication and Authorization

---

## Objective

Strengthen the backend by implementing secure user authentication and authorization. The goal of this phase was to protect application resources, establish user identity, and ensure that users could only access data associated with their own accounts.

---

## Implementation

Authentication was introduced using JSON Web Tokens (JWT), allowing users to securely access protected resources after successfully logging into the system. Passwords were secured using bcrypt hashing before being stored in the database, ensuring that sensitive credentials were never saved in plain text.

A complete authentication workflow was implemented, including user registration, login, token generation, and token validation. Once authenticated, users receive a JWT that is required to access protected endpoints.

To simplify authorization across the application, reusable authentication dependencies were introduced. These dependencies validate incoming tokens, identify the authenticated user, and make user information available throughout the request lifecycle without duplicating code.

The booking module was updated to integrate with the authentication system. Rather than allowing unrestricted access, bookings became associated with the currently authenticated user. Additional validation was added to ensure users could only create, view, and manage their own bookings.

A dedicated endpoint was also implemented to retrieve the authenticated user's booking history, providing a centralized view of all reservations associated with the current account.

---

## Deliverables

* User registration endpoint.
* Secure login endpoint.
* JWT authentication.
* Bcrypt password hashing.
* Token validation.
* Authentication dependency.
* Protected API endpoints.
* Current authenticated user extraction.
* User-specific booking ownership.
* User booking history endpoint.
* Swagger authentication support.

---

## Testing

The authentication workflow was verified using Swagger UI. User registration, login, token generation, and protected endpoints were tested under both valid and invalid authentication scenarios. Booking ownership validation was also tested to confirm that users could not access or manage reservations belonging to other accounts.

---

## Outcome

Phase 4 introduced a complete authentication and authorization layer for the application. User identities are now securely verified before accessing protected resources, and ownership validation ensures that each user can interact only with data associated with their own account. This established the security foundation required for future administrative functionality.
