import json
import logging
from datetime import datetime, timezone
from logging.config import dictConfig

from app.core.config import settings


class JsonFormatter(logging.Formatter):
    def format(self, record):
        log_data = {
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "level": record.levelname,
            "logger": record.name,
            "message": record.getMessage()
        }

        if hasattr(record, "request_id"):
            log_data["request_id"] = record.request_id

        if hasattr(record, "method"):
            log_data["method"] = record.method

        if hasattr(record, "path"):
            log_data["path"] = record.path

        if hasattr(record, "status_code"):
            log_data["status_code"] = record.status_code

        if hasattr(record, "duration_ms"):
            log_data["duration_ms"] = record.duration_ms

        if hasattr(record, "environment"):
            log_data["environment"] = record.environment

        if record.exc_info:
            log_data["exception"] = self.formatException(
                record.exc_info
            )

        return json.dumps(
            log_data,
            ensure_ascii=False
        )


def configure_logging():
    dictConfig({
        "version": 1,
        "disable_existing_loggers": False,

        "formatters": {
            "json": {
                "()": "app.core.logging_config.JsonFormatter"
            }
        },

        "handlers": {
            "console": {
                "class": "logging.StreamHandler",
                "formatter": "json"
            }
        },

        "root": {
            "handlers": ["console"],
            "level": settings.LOG_LEVEL.upper()
        },

        "loggers": {
            "app": {
                "handlers": ["console"],
                "level": settings.LOG_LEVEL.upper(),
                "propagate": False
            }
        }
    })