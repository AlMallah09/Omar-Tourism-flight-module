# Development Log – Phase 4

## Phase Title

Authentication and Authorization

---

## Objective

Implement a secure authentication system and integrate authorization throughout the application to protect business operations and user data.

---

## Activities Completed

* Implemented secure user registration.
* Implemented user login.
* Integrated bcrypt password hashing.
* Implemented JWT token generation.
* Added JWT token validation.
* Created authentication dependencies.
* Protected secured API endpoints.
* Implemented authenticated user retrieval.
* Linked bookings to authenticated users.
* Restricted booking operations to resource owners.
* Added endpoint for retrieving authenticated user's bookings.
* Configured Swagger authentication support.
* Verified complete authentication workflow.

---

## Challenges Encountered

Authentication affected multiple modules simultaneously. Once protected endpoints were introduced, existing booking operations had to be updated to work with authenticated users while preserving the existing business logic.

---

## Solutions Applied

Authentication responsibilities were centralized into reusable utility functions and dependencies. This avoided duplicate authentication logic across endpoints while allowing authorization rules to be applied consistently throughout the application.

---

## Technical Decisions

* Adopted JWT for stateless authentication.
* Used bcrypt for password hashing.
* Implemented reusable authentication dependencies.
* Applied ownership validation to booking operations.
* Continued separating authentication, routing, and business logic into dedicated modules.

---

## Outcome

The backend now supports secure authentication, protected resources, and user-based authorization. Sensitive operations require valid authentication, and access control is enforced consistently across the booking workflow.

---

## Next Phase

Extend the booking system by introducing passenger management, allowing each booking to maintain passenger information, travel documentation, and ticket details while preserving ownership validation and booking integrity.
