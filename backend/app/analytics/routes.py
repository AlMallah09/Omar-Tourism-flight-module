from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.authentication.utils import admin_required
from app.users.models import User

from app.analytics import services
from app.analytics.schemas import (
    AnalyticsDashboard,
    DestinationStat,
    FlightOccupancyStat,
    MonthlyAnalytics,
    RevenueAnalytics,
    BookingAnalytics,
    FlightAnalytics,
    OriginStat,
    RouteStat,
    CustomerAnalytics,
    TopCustomerStat,
    FlightPerformanceStat,
    CustomerGrowthStat,
    KPIAnalytics,
)

router = APIRouter(
    prefix="/analytics",
    tags=["Analytics"]
)


@router.get(
    "/revenue",
    response_model=RevenueAnalytics
)
def revenue_analytics(
    db: Session = Depends(get_db),
    current_admin: User = Depends(admin_required)
):
    return services.get_revenue_analytics(db)


@router.get(
    "/bookings",
    response_model=BookingAnalytics
)
def booking_analytics(
    db: Session = Depends(get_db),
    current_admin: User = Depends(admin_required)
):
    return services.get_booking_analytics(db)


@router.get(
    "/flights",
    response_model=FlightAnalytics
)
def flight_analytics(
    db: Session = Depends(get_db),
    current_admin: User = Depends(admin_required)
):
    return services.get_flight_analytics(db)


@router.get(
    "/destinations",
    response_model=list[DestinationStat]
)
def destination_analytics(
    db: Session = Depends(get_db),
    current_admin: User = Depends(admin_required)
):
    return services.get_top_destinations(db)


@router.get(
    "/origins",
    response_model=list[OriginStat]
)
def origin_analytics(
    db: Session = Depends(get_db),
    current_admin: User = Depends(admin_required)
):
    return services.get_top_origins(db)


@router.get(
    "/routes",
    response_model=list[RouteStat]
)
def route_analytics(
    db: Session = Depends(get_db),
    current_admin: User = Depends(admin_required)
):
    return services.get_top_routes(db)


@router.get(
    "/customers",
    response_model=CustomerAnalytics
)
def customer_analytics(
    db: Session = Depends(get_db),
    current_admin: User = Depends(admin_required)
):
    return services.get_customer_analytics(db)


@router.get(
    "/customers/top",
    response_model=list[TopCustomerStat]
)
def top_customers(
    db: Session = Depends(get_db),
    current_admin: User = Depends(admin_required)
):
    return services.get_top_customers(db)


@router.get(
    "/dashboard",
    response_model=AnalyticsDashboard
)
def analytics_dashboard(
    db: Session = Depends(get_db),
    current_admin: User = Depends(admin_required)
):
    return services.get_analytics_dashboard(db)


@router.get(
    "/monthly",
    response_model=list[MonthlyAnalytics]
)
def monthly_analytics(
    db: Session = Depends(get_db),
    current_admin: User = Depends(admin_required)
):
    return services.get_monthly_analytics(db)


@router.get(
    "/flights/top",
    response_model=list[FlightPerformanceStat]
)
def top_flights(
    db: Session = Depends(get_db),
    current_admin: User = Depends(admin_required)
):
    return services.get_top_flights(db)


@router.get(
    "/customers/growth",
    response_model=list[CustomerGrowthStat]
)
def customer_growth(
    db: Session = Depends(get_db),
    current_admin: User = Depends(admin_required)
):
    return services.get_customer_growth(db)


@router.get(
    "/kpis",
    response_model=KPIAnalytics
)
def kpi_analytics(
    db: Session = Depends(get_db),
    current_admin: User = Depends(admin_required)
):
    return services.get_kpi_analytics(db)


@router.get(
    "/flights/occupancy",
    response_model=list[FlightOccupancyStat]
)
def flight_occupancy(
    db: Session = Depends(get_db),
    current_admin: User = Depends(admin_required)
):
    return services.get_flight_occupancy(db)