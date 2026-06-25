# Changelog

All notable changes to this project are documented in this file.

The format follows a simplified version of the Keep a Changelog specification.

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
