# Changelog

All notable changes to this project are documented in this file.

The format follows a simplified version of the Keep a Changelog specification.

---

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
