from pydantic import BaseModel


class RevenueAnalytics(BaseModel):
    total_revenue: float
    paid_revenue: float
    refunded_amount: float
    average_booking_value: float


class BookingAnalytics(BaseModel):
    total_bookings: int
    confirmed_bookings: int
    cancelled_bookings: int
    paid_bookings: int
    refunded_bookings: int
    cancellation_rate: float


class FlightAnalytics(BaseModel):
    total_flights: int
    active_flights: int
    cancelled_flights: int
    total_seats_available: int
    total_bookings: int
    average_bookings_per_flight: float

class DestinationStat(BaseModel):
    destination: str
    bookings: int


class OriginStat(BaseModel):
    origin: str
    bookings: int


class RouteStat(BaseModel):
    origin: str
    destination: str
    bookings: int


class CustomerAnalytics(BaseModel):
    total_customers: int
    customers_with_bookings: int
    customers_without_bookings: int
    average_bookings_per_customer: float


class TopCustomerStat(BaseModel):
    user_id: int
    email: str
    bookings: int
    total_spent: float


class AnalyticsDashboard(BaseModel):
    total_revenue: float
    paid_revenue: float
    refunded_amount: float
    average_booking_value: float

    total_bookings: int
    confirmed_bookings: int
    cancelled_bookings: int
    cancellation_rate: float

    total_flights: int
    active_flights: int
    cancelled_flights: int

    total_customers: int
    customers_with_bookings: int
    customers_without_bookings: int


class MonthlyAnalytics(BaseModel):
    month: str
    bookings: int
    revenue: float


class FlightPerformanceStat(BaseModel):
    flight_id: int
    airline: str
    origin: str
    destination: str
    confirmed_bookings: int
    passengers_booked: int


class CustomerGrowthStat(BaseModel):
    month: str
    new_customers: int


class KPIAnalytics(BaseModel):
    paid_revenue: float
    total_bookings: int
    cancellation_rate: float
    active_flights: int
    total_customers: int
    customers_with_bookings: int


class FlightOccupancyStat(BaseModel):
    flight_id: int
    airline: str
    origin: str
    destination: str
    total_seats: int
    seats_available: int
    booked_seats: int
    occupancy_rate: float