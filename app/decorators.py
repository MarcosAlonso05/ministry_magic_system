import logging
import functools
import sys
from fastapi import HTTPException

from app.data.magic_catalog import SPELL_DATA, EVENT_DATA

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("docs/ministry_audit.log"),
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger("MinistryLog")

def validate_magic_permission(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        user = kwargs.get('user')
        magic_name = kwargs.get('magic_name')
        is_event = kwargs.get('is_event', False)

        if not user or not magic_name:
            raise HTTPException(status_code=400, detail="Missing context (user or magic name).")

        if is_event:
            catalog = EVENT_DATA
            catalog_type = "Event"
        else:
            catalog = SPELL_DATA
            catalog_type = "Spell"

        found_key = next((k for k in catalog.keys() if k.lower() == magic_name.lower()), None)

        if not found_key:
            logger.error(f"SECURITY: Unknown magic '{magic_name}' requested by {user.username}.")
            raise HTTPException(status_code=404, detail=f"{catalog_type} '{magic_name}' not found in Ministry records.")

        required_perm = catalog[found_key]['perm']

        if not user.has_permission(required_perm):
            logger.warning(f"SECURITY: Access Denied. {user.username} (Role: {user.role}) tried to cast '{found_key}' which requires '{required_perm}'.")
            raise HTTPException(status_code=403, detail=f"Forbidden: This magic requires '{required_perm}' clearance.")

        return func(*args, **kwargs)

    return wrapper

def audit_log(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        user = kwargs.get('user')
        username = user.username if user else "Unknown"
        magic_name = kwargs.get('magic_name', 'Unknown')

        logger.info(f"AUDIT [START]: Wizard '{username}' invoking '{magic_name}'...")
        try:
            result = func(*args, **kwargs)
            logger.info(f"AUDIT [SUCCESS]: '{magic_name}' performed.")
            return result
        except Exception as e:
            logger.error(f"AUDIT [FAILURE]: '{magic_name}' failed. Error: {str(e)}")
            raise e
    return wrapper

def magic_transaction(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            logger.critical("TRANSACTION: Rolling back magic changes due to error.")
            raise e
    return wrapper