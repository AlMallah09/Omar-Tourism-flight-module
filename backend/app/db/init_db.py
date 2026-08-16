from alembic import command
from alembic.config import Config
from sqlalchemy import create_engine, inspect

from app.core.config import settings
from app.db.base import Base

import app.users.models
import app.flights.models
import app.bookings.models
import app.passengers.models
import app.admin.models
import app.authentication.models


def initialize_database():
    engine = create_engine(settings.DATABASE_URL)

    inspector = inspect(engine)

    existing_tables = set(
        inspector.get_table_names()
    )

    application_tables = existing_tables - {
        "alembic_version"
    }

    alembic_config = Config("alembic.ini")

    if not application_tables:
        Base.metadata.create_all(bind=engine)

        command.stamp(
            alembic_config,
            "head"
        )

    else:
        command.upgrade(
            alembic_config,
            "head"
        )


if __name__ == "__main__":
    initialize_database()