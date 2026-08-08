# Development Log – Phase 6.4

## Phase Title

Analytics and Business Intelligence

---

## Objective

Introduce a dedicated analytics and business intelligence layer that transforms existing flight, booking, payment, customer, and passenger data into meaningful administrative metrics while maintaining the modular structure, security, and consistency of the backend.

---

## Activities Completed

* Created a dedicated analytics module with separate routes, services, and schemas.
* Integrated the analytics router into the main FastAPI application.
* Protected analytics functionality using administrator-only authorization.
* Implemented revenue analytics including total revenue, paid revenue, refunded amounts, and average booking value.
* Implemented booking analytics with booking totals, status statistics, and cancellation rates.
* Implemented flight analytics with operational flight statistics.
* Added destination analytics based on booking activity.
* Added origin analytics based on booking activity.
* Implemented route performance analytics.
* Added customer analytics with booking participation and average booking statistics.
* Implemented top-customer ranking using booking volume and customer spending.
* Excluded administrative accounts from customer-specific analytics.
* Added monthly customer growth analytics.
* Added monthly booking and revenue trend analytics.
* Implemented individual flight performance analytics.
* Added passenger-volume analysis for flight performance.
* Added identification of flights with no bookings.
* Implemented a consolidated analytics dashboard endpoint.
* Added a dedicated KPI endpoint for high-level business metrics.
* Extended the flight model with total seat capacity.
* Updated flight creation to initialize available seats automatically from total capacity.
* Removed direct seat availability manipulation from normal flight updates.
* Added validation for flight capacity changes while preserving existing bookings.
* Prevented flight capacity from being reduced below already booked seats.
* Implemented flight occupancy and seat utilization analytics.
* Added booked-seat and occupancy-rate calculations.
* Verified all analytics endpoints using Swagger UI.

---

## Challenges Encountered

The analytics layer depended heavily on data and business rules introduced throughout previous phases. Revenue, booking, customer, flight, and route calculations had to remain consistent with the existing operational workflows while being presented through a separate analytical interface.

Separating analytics from the administration module also required restructuring the router organization after analytics endpoints initially appeared under overlapping Swagger sections.

Another important limitation appeared while implementing seat utilization. The original flight model stored only remaining seat availability, which was sufficient for booking operations but did not preserve the original capacity required to calculate accurate occupancy rates.

Customer analytics also required additional filtering to prevent administrative accounts from being treated as customers and affecting business statistics.

---

## Solutions Applied

Analytics functionality was separated into a dedicated module containing its own routes, schemas, and service logic. The analytics router was registered independently, providing a clear separation between administrative management operations and business intelligence.

Existing operational data was aggregated dynamically rather than duplicating statistics in additional database tables. Customer queries were refined to exclude administrative users where customer-specific metrics were calculated.

The flight model was extended with `total_seats` to preserve original capacity independently from `seats_available`. New flights automatically initialize available inventory from total capacity, while capacity updates calculate already booked seats before modifying availability.

Validation prevents administrators from reducing flight capacity below existing booked-seat counts, preserving reservation consistency while allowing legitimate capacity adjustments.

---

## Technical Decisions

* Created a dedicated analytics module instead of expanding the administration module further.
* Reused existing authentication and `admin_required` authorization controls.
* Calculated analytical metrics dynamically from operational database records.
* Kept analytics logic within the service layer.
* Used PostgreSQL aggregation through SQLAlchemy for business metrics.
* Excluded administrative accounts from customer-specific analytics.
* Used passenger volume alongside booking counts for flight performance.
* Added monthly aggregation to support future dashboard charts.
* Added consolidated dashboard and KPI endpoints for future frontend integration.
* Introduced `total_seats` as persistent flight capacity.
* Prevented direct modification of `seats_available` through normal flight updates.
* Preserved booked-seat counts when flight capacity changes.
* Calculated occupancy dynamically instead of storing derived occupancy values.
* Continued following the modular architecture by separating routes, services, models, and schemas.

---

## Outcome

The backend now provides a dedicated business intelligence layer capable of analyzing revenue, bookings, flights, customers, destinations, routes, monthly trends, flight performance, and seat utilization.

Phase 6.4 also improved the underlying flight inventory model by separating total capacity from remaining availability. This allows reservation operations and occupancy analytics to use the same flight data without compromising consistency.

The analytics APIs establish the backend foundation required for KPI cards, charts, rankings, operational insights, and other analytical components in the future administrative dashboard.

---

## Next Phase

Introduce reporting and export capabilities by implementing structured business reports, downloadable datasets, administrative exports, and reusable reporting services based on the operational and analytical data established throughout the previous phases.