# Technical Decisions

## Backend Framework

Python with FastAPI will be used for backend development.

## Reason for Choosing FastAPI

FastAPI was selected because:
- The backend was requested to be built in Python.
- It is modern and suitable for REST API development.
- It provides automatic API documentation.
- It supports clean and scalable backend architecture.
- It works well with PostgreSQL and third-party API integration.

## Database

PostgreSQL will be used as the database system.

Reasons:
- Reliable relational database.
- Suitable for structured booking data.
- Supports constraints and relationships.
- Scalable for future modules such as hotels.

## Mobile Application

Flutter will be used for the mobile application.

Reasons:
- One codebase for iOS and Android.
- Suitable for business applications.
- Can easily consume REST APIs.

## Data Strategy

The first version will use mock/sample data.

This allows:
- Backend development before provider selection.
- API testing.
- Mobile app testing.
- Booking flow simulation.

Future versions can connect to official third-party APIs.