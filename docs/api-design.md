# API Design

## Purpose

This document defines the initial API structure for the flight management and booking backend.

The APIs will be built using Python FastAPI.

## Authentication APIs

POST /auth/register  
POST /auth/login  

## User APIs

GET /users/me  
PUT /users/me  

## Flight APIs

GET /flights  
GET /flights/{flight_id}  
POST /flights  
PUT /flights/{flight_id}  
DELETE /flights/{flight_id}  

## Booking APIs

POST /bookings  
GET /bookings/my-bookings  
GET /bookings/{booking_id}  
PUT /bookings/{booking_id}/cancel  

## Admin APIs

GET /admin/bookings  
GET /admin/flights  
GET /admin/reports  

## Future Provider Integration APIs

GET /providers/flights/search  
POST /providers/bookings/confirm  

These endpoints are planned for future integration with official third-party flight or hotel providers.