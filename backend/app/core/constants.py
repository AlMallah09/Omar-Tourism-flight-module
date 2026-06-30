from enum import Enum

class BookingStatus(str, Enum):
    CONFIRMED = "confirmed"
    CANCELLED = "cancelled"

class PaymentStatus(str, Enum):
    UNPAID = "unpaid"
    PENDING = "pending"
    PAID = "paid"
    FAILED = "failed"
    REFUNDED = "refunded"

class FlightStatus(str, Enum):
    SCHEDULED = "scheduled"
    CANCELLED = "cancelled"