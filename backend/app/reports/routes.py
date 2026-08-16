from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import StreamingResponse
from sqlalchemy.orm import Session
import io

from app.db.database import get_db
from app.authentication.utils import admin_required
from app.users.models import User

from app.reports import services

from datetime import datetime, date

router = APIRouter(
    prefix="/reports",
    tags=["Reports"]
)

@router.get("/bookings/excel")
def export_bookings_excel(
    start_date: date | None = None,
    end_date: date | None = None,
    db: Session = Depends(get_db),
    current_admin: User = Depends(admin_required)
):
    if start_date and end_date and end_date < start_date:
        raise HTTPException(
            status_code=400,
            detail="End date cannot be earlier than start date"
        )

    excel_file = services.generate_bookings_excel(
        db,
        start_date,
        end_date
    )

    return StreamingResponse(
        excel_file,
        media_type=(
            "application/vnd.openxmlformats-officedocument."
            "spreadsheetml.sheet"
        ),
        headers={
            "Content-Disposition":
                'attachment; filename="bookings_report.xlsx"'
        }
    )


@router.get("/flights/excel")
def export_flights_excel(
    db: Session = Depends(get_db),
    current_admin: User = Depends(admin_required)
):
    excel_file = services.generate_flights_excel(db)

    return StreamingResponse(
        excel_file,
        media_type=(
            "application/vnd.openxmlformats-officedocument."
            "spreadsheetml.sheet"
        ),
        headers={
            "Content-Disposition":
                'attachment; filename="flights_report.xlsx"'
        }
    )

@router.get("/customers/excel")
def export_customers_excel(
    db: Session = Depends(get_db),
    current_admin: User = Depends(admin_required)
):
    excel_file = services.generate_customers_excel(db)

    return StreamingResponse(
        excel_file,
        media_type=(
            "application/vnd.openxmlformats-officedocument."
            "spreadsheetml.sheet"
        ),
        headers={
            "Content-Disposition":
                'attachment; filename="customers_report.xlsx"'
        }
    )


@router.get("/revenue/excel")
def export_revenue_excel(
    db: Session = Depends(get_db),
    current_admin: User = Depends(admin_required)
):
    excel_file = services.generate_revenue_excel(db)

    return StreamingResponse(
        excel_file,
        media_type=(
            "application/vnd.openxmlformats-officedocument."
            "spreadsheetml.sheet"
        ),
        headers={
            "Content-Disposition":
                'attachment; filename="revenue_report.xlsx"'
        }
    )


@router.get("/business/excel")
def export_business_report_excel(
    start_date: date | None = None,
    end_date: date | None = None,
    db: Session = Depends(get_db),
    current_admin: User = Depends(admin_required)
):
    if start_date and end_date and end_date < start_date:
        raise HTTPException(
            status_code=400,
            detail="End date cannot be earlier than start date"
        )

    excel_file = services.generate_business_report_excel(
        db,
        start_date,
        end_date
    )

    return StreamingResponse(
        excel_file,
        media_type=(
            "application/vnd.openxmlformats-officedocument."
            "spreadsheetml.sheet"
        ),
        headers={
            "Content-Disposition":
                'attachment; filename="omar_tourism_business_report.xlsx"'
        }
    )