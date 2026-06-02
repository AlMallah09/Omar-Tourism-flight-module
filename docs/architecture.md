# System Architecture

## Overview

The Flight Booking System will use a centralized backend architecture.

### Components

* Existing Website
* Flutter Mobile Application (iOS & Android)
* Node.js Backend API
* PostgreSQL Database

### Data Flow

Website → Backend API → Database

Mobile App → Backend API → Database

The backend will serve as the single source of truth for all flight and booking data.
