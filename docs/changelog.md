# Changelog

All notable changes to this project are documented in this file.

The format follows a simplified version of the Keep a Changelog specification.

## v0.6.6 – Production Readiness

### Added
- Alembic database migration framework.
- Existing-schema baseline migration.
- Database revision tracking through `alembic_version`.
- Fresh-database initialization and Alembic stamping.
- Centralized environment-backed application configuration.
- Environment configuration for JWT security, API versioning, logging, CORS, and trusted hosts.
- `.env.example` and Docker environment example configuration.
- Global HTTP exception handling.
- Global request-validation handling.
- Controlled internal server-error responses.
- Structured JSON-style application logging.
- Request IDs and `X-Request-ID` response headers.
- Request execution-time logging.
- Configurable CORS middleware.
- Trusted-host validation.
- HTTP security response headers.
- `/api/v1` API version namespace.
- Multi-stage FastAPI Docker image.
- Docker Compose environment for FastAPI and PostgreSQL.
- PostgreSQL container health checking.
- Persistent PostgreSQL Docker volume.
- Database initialization before API startup.
- Docker-specific environment configuration.
- Container runtime dependency verification.

### Changed
- Moved JWT secret, algorithm, and access-token expiration from source code into environment configuration.
- Updated JWT expiration timestamps to timezone-aware UTC values.
- Updated OAuth2 authentication configuration for the versioned API.
- Standardized error responses across the backend.
- Centralized repeated runtime configuration in `app/core`.
- Updated application startup to support database initialization and migration before Uvicorn startup.
- Expanded `requirements.txt` to represent dependencies required by a clean deployment environment.

### Security
- Removed the JWT signing secret from application source code.
- Added trusted-host protection.
- Added configurable CORS restrictions.
- Added `X-Content-Type-Options`, `X-Frame-Options`, and `Referrer-Policy` response headers.
- Prevented unexpected internal exception details from being exposed directly to API clients.
- Kept authentication tokens, passwords, database credentials, and application secrets out of structured request logs.

---

## v0.6.5 – Reports and Exports

### Added
- Dedicated reports module.
- Administrator-only Excel report endpoints.
- Booking Excel reports with optional start-date and end-date filtering.
- Flight Excel reports.
- Customer Excel reports with booking counts and booking value totals.
- Revenue Excel reports.
- Combined business management workbook.
- Executive Summary worksheet.
- Business Analytics worksheet.
- Reporting-period support for combined reports.
- Date-range validation.
- Flight occupancy and capacity reporting.
- Timezone-safe Excel datetime conversion.
- Reusable Excel formatting and workbook utilities.
- `openpyxl` dependency for spreadsheet generation.

### Changed
- Standardized business report output around Excel `.xlsx` files.
- Replaced the initial CSV export implementation with formatted Excel reporting.
- Simplified reporting-period input from full timestamps to standard dates.
- Applied reporting periods consistently across applicable business report calculations.
- Consolidated repeated workbook formatting logic into reusable reporting utilities.

### Security
- Restricted all reporting and export endpoints to authenticated administrators.

---

## v0.6.4 – Analytics and Business Intelligence

### Added

* Dedicated `analytics` module.
* Revenue analytics.
* Booking analytics.
* Flight analytics.
* Customer analytics.
* Customer growth tracking.
* Destination and origin analytics.
* Route performance analytics.
* Monthly booking and revenue trends.
* Flight performance analytics.
* Flights-without-bookings analysis.
* Flight occupancy and seat utilization analytics.
* Consolidated analytics dashboard endpoint.
* Key Performance Indicator (KPI) endpoint.
* Total flight capacity tracking through `total_seats`.

### Changed

* Separated analytics functionality from the administration module.
* Extended the flight model to distinguish total capacity from available seats.
* Updated flight creation to initialize `seats_available` automatically from `total_seats`.
* Updated flight capacity changes to preserve already booked seats.
* Removed direct modification of `seats_available` from normal flight updates.
* Excluded administrative accounts from customer-specific analytics.
* Expanded the backend with business intelligence capabilities for future dashboard integration.

### Security

* Restricted analytics endpoints to authorized administrators.
* Prevented flight capacity from being reduced below already booked seats.
* Preserved booking and seat inventory consistency during flight capacity changes.

---

## v0.6.3 – Advanced Administration

### Added

* Administrator-only flight creation and updates.
* Flight soft cancellation and restoration.
* Administrative access to all flight records.
* Advanced flight filtering.
* Advanced booking filtering.
* Booking status management.
* Payment status management.
* Booking refund functionality.
* Expanded administrative dashboard statistics.
* Recent activity endpoint.
* System health endpoint.
* Audit log retrieval endpoint.
* Pagination for administrative endpoints.
* Centralized application status constants.
* Enum validation for booking, payment, and flight statuses.
* Standardized administrative API responses.

### Changed

* Expanded the administration module with advanced flight and booking management.
* Replaced permanent flight deletion with soft cancellation.
* Prevented cancelled flights from appearing in public flight listings.
* Improved administrative filtering and request validation.
* Centralized repeated status values to improve maintainability.
* Refined administrative API responses for consistency.
* Cleaned temporary debugging code and unused imports.

### Security

* Restricted flight creation and modification to authorized administrators.
* Centralized administrative authorization using `admin_required`.
* Enforced valid booking and payment status combinations.
* Added validation for administrative flight and booking operations.

---


## v0.6.2 — Password and Account Security

### Added

* Change password functionality.
* Password strength validation.
* Password history tracking.
* Password reuse prevention.
* Administrator password reset.
* Forced password change after administrator reset.
* Last login tracking.
* Failed login attempt tracking.
* Automatic account lockout.
* Administrator account unlock endpoint.
* Forgot-password workflow.
* Password reset token model.
* Reset password using secure tokens.
* Single-use password reset tokens.
* Automatic invalidation of previous reset tokens.
* Expired password reset token cleanup endpoint.

### Changed

* Extended the User model with additional account security fields.
* Improved authentication workflow with login tracking and password management.
* Centralized password validation and security logic within the authentication service.

### Security

* Passwords cannot be reused from recent history.
* Accounts are automatically locked after repeated failed login attempts.
* Password reset tokens expire automatically.
* Only the latest unused reset token remains valid.
* Password-related actions are recorded in the audit log.

## v0.6.1 — Administration Foundation

### Added

* Role-Based Access Control (RBAC).
* Administrator authorization dependency.
* Dedicated `admin` module.
* Administrative dashboard endpoint.
* Dashboard statistics service.
* Audit Log database model.
* Audit logging service.
* Automatic logging for administrative actions.
* User administration endpoints.
* Booking administration endpoints.
* User search functionality.
* Account enable and disable operations.
* Soft delete and account restoration.

### Changed

* Refactored administrative functionality into the dedicated `app/admin` module.
* Moved dashboard implementation from the authentication module.
* Centralized dashboard statistics through the administration service layer.
* Reorganized administrative routes to improve maintainability.

### Security

* Restricted administrative endpoints to authorized administrators.
* Prevented disabled accounts from authenticating.
* Prevented soft-deleted accounts from authenticating.
* Added complete audit trail for administrative operations.
