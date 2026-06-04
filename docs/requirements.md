# Requirements Analysis

## Scope

The scope is limited to the flight management and booking backend system.

The first version will use mock/sample data. Real-time flight pricing, availability, and confirmation will require future integration with official third-party APIs.

## Customer Requirements

Customers should be able to:
- Register
- Log in
- Search flights
- View flight details
- Create bookings
- View their bookings
- Cancel bookings

## Admin Requirements

Admins should be able to:
- Add flights
- Update flights
- Delete flights
- View bookings
- Manage availability
- Review operational data

## System Requirements

The system should:
- Provide APIs for web and mobile clients.
- Store data in PostgreSQL.
- Use Python FastAPI.
- Support mock data initially.
- Be designed for future third-party API integration.
- Keep the structure simple, practical, and manageable.