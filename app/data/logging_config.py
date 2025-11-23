import os

os.makedirs("logs", exist_ok=True)

LOGGING_CONFIG = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "standard": {
            "format": "%(asctime)s [%(levelname)s] %(name)s: %(message)s"
        },
        "detailed": {
            "format": "%(asctime)s - %(name)s - %(levelname)s - %(module)s:%(lineno)d - %(message)s"
        },
    },
    "handlers": {
        "console": {
            "level": "INFO",
            "class": "logging.StreamHandler",
            "formatter": "standard",
        },
        "file_audit": {
            "level": "INFO",
            "class": "logging.FileHandler",
            "filename": "logs/ministry_audit.log",
            "formatter": "detailed",
            "encoding": "utf-8",
        },
        "file_errors": {
            "level": "ERROR",
            "class": "logging.FileHandler",
            "filename": "logs/ministry_errors.log",
            "formatter": "detailed",
            "encoding": "utf-8",
        },
    },
    "loggers": {
        "MinistryLog": {
            "handlers": ["console", "file_audit", "file_errors"],
            "level": "INFO",
            "propagate": False,
        },
        "uvicorn": {
            "handlers": ["console"],
            "level": "INFO",
        },
    },
}