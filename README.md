# Flight Management and Booking Module

## Overview

This repository contains technical documentation, planning, and backend preparation work for the flight management and booking segment of Omar Tourism.

The system will be developed using Python and FastAPI. It will provide APIs that can be used by a future mobile application and can later be integrated with the existing WordPress website.

## Confirmed System Context

The existing company website is built using WordPress with the Traveler theme.

Currently:
- There is no separate custom backend.
- There is no separate custom database.
- Flight booking is handled through a third-party platform/service.
- The exact third-party provider is still to be confirmed.

## Development Direction

The backend will first be built using mock/sample data, a database, admin-side management, booking flow, and API endpoints.

Later, if an official flight or hotel provider is selected, the same backend structure can be extended to connect with the provider's API.

## Technology Stack

- Python
- FastAPI
- PostgreSQL
- Flutter
- GitHub

## Repository Structure

- backend/ → FastAPI backend implementation
- docs/ → Technical documentation
- diagrams/ → System diagrams