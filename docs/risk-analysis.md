# Risk Analysis

## Risk 1: Third-Party Provider Not Confirmed

The exact flight booking provider is not yet confirmed.

Impact:
- Real-time pricing and availability cannot be implemented immediately.

Mitigation:
- Use mock/sample data first.
- Design the backend so provider integration can be added later.

## Risk 2: Website Integration Unclear

The existing website is WordPress with the Traveler theme.

Impact:
- Direct integration approach may depend on WordPress capabilities.

Mitigation:
- Build independent APIs first.
- Later decide whether to integrate through WordPress plugins, custom API calls, or separate frontend components.

## Risk 3: Scope Expansion

The system may later include hotels.

Impact:
- Poor backend structure could make expansion difficult.

Mitigation:
- Use modular architecture from the start.
- Separate flight, booking, user, and provider logic.

## Risk 4: Data Accuracy

Mock/sample data does not represent real provider availability.

Impact:
- Initial system cannot confirm real bookings.

Mitigation:
- Clearly document that mock data is for development and testing.
- Keep provider integration as a future phase.

## Risk 5: Security Issues

User and booking data must be protected.

Impact:
- Poor security can expose sensitive information.

Mitigation:
- Use password hashing.
- Use JWT authentication.
- Protect admin endpoints.
- Store secrets in environment variables.