# Phase 6.5 Report

## Phase Title
Reports and Exports

---

## Objective
The objective of Phase 6.5 was to provide administrators with a structured reporting layer for operational, financial, customer, and business data. The reporting system was designed to convert information already available through the booking, flight, user, payment, and analytics modules into downloadable Excel reports that can be reviewed outside the API environment.

The phase also focused on keeping reporting logic independent from the analytics and administration modules so that report generation could be maintained and extended without increasing coupling across the backend.

---

## Work Completed

### Reporting Module
A dedicated `reports` module was introduced to contain report routes, services, schemas, and export-related logic.

The module follows the same modular structure used throughout the backend and is protected through the existing administrator authorization dependency.

### Booking Reports
An Excel booking report was implemented containing booking, customer, flight, payment, and pricing information.

Administrators can optionally provide a start date and end date to generate reports for a specific booking period. When no dates are supplied, the report returns all available booking records.

Date-range validation was also added to prevent an end date from being earlier than the selected start date.

### Flight Reports
A downloadable flight report was implemented containing flight identification, airline, route, departure and arrival times, pricing, seat capacity, seat availability, and current flight status.

Timezone-aware datetime values are converted into an Excel-compatible representation during export without changing the values stored in the database.

### Customer Reports
A customer report was implemented to summarize customer activity.

The report includes customer identification, email address, total bookings, and total booking value. Administrator accounts are excluded so that the report represents actual customer activity only.

### Revenue Reports
A financial report was implemented to summarize booking-related financial information.

The report includes total booking value, paid revenue, refunded amounts, total booking count, and average booking value.

Payment calculations use the centralized payment status definitions already established in the backend.

### Combined Business Report
A complete management-oriented Excel workbook was implemented to combine the main reporting areas into a single downloadable file.

The workbook contains the following worksheets:

- Executive Summary
- Bookings
- Flights
- Customers
- Revenue
- Business Analytics

The Executive Summary provides a consolidated view of booking volumes, cancellation rates, revenue, customer activity, flight capacity, booked seats, and occupancy.

### Reporting Period Support
The combined business report supports optional start and end dates.

When a reporting period is selected, applicable booking, revenue, customer activity, flight, occupancy, and business analytics calculations are generated for that period.

When no dates are supplied, the workbook operates as an all-time business report.

### Excel Export and Formatting
Excel reports are generated dynamically in memory using `openpyxl`.

Reusable formatting utilities were introduced for header formatting, column sizing, workbook serialization, date filtering, and datetime conversion.

This avoids storing temporary report files on the backend server and reduces duplicated formatting logic across the reporting services.

### Administrator Protection
All report endpoints require administrator authorization through the existing centralized `admin_required` dependency.

This prevents normal customer accounts and unauthenticated users from downloading internal operational and financial reports.

---

## Results
Phase 6.5 introduced a complete reporting layer that allows administrators to convert backend operational data into structured Excel workbooks.

Individual reports can be generated for bookings, flights, customers, and revenue, while the combined business report provides a management-level view of the system through multiple worksheets and consolidated business metrics.

The reporting system uses the existing database and business rules directly, supports reporting periods where applicable, and maintains the modular architecture established in previous phases.

All reporting endpoints were verified successfully through Swagger UI, including report generation, Excel formatting, date filtering, invalid date-range handling, and administrator authorization.

---

## Deliverables
- Dedicated reports module
- Booking Excel report
- Optional booking date filtering
- Flight Excel report
- Customer Excel report
- Revenue Excel report
- Combined business Excel workbook
- Executive summary reporting
- Business analytics worksheet
- Reporting-period support
- Date-range validation
- Excel-compatible datetime handling
- Reusable report formatting utilities
- Administrator-only report access
- `openpyxl` integration
- Swagger verification of report endpoints

---

## Phase Status
**Completed Successfully**

**Release Version:** `v0.6.5`

**Release Name:** **Reports and Exports Complete**

---

## Next Phase
Phase 6.6 will focus on Production Readiness. The backend will be prepared for a more controlled deployment environment through database migrations, containerization, configuration management, logging, API organization, security improvements, and centralized error handling.