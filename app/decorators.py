import logging
import functools
from fastapi import HTTPException

# Configure Logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("MinistryLog")

def audit_log(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # 1. Extract info for the log (Safe extraction)
        user = kwargs.get('user')
        username = user.username if user else "Unknown"
        magic_name = kwargs.get('magic_name', 'Unknown Magic')

        # 2. LOG BEFORE: The wizard is about to start
        logger.info(f"AUDIT: User '{username}' is invoking '{magic_name}'...")

        try:
            # 3. EXECUTE THE REAL FUNCTION
            # This is the moment the spell is actually cast
            result = func(*args, **kwargs)
            
            # 4. LOG AFTER (SUCCESS)
            logger.info(f"AUDIT: Success. '{magic_name}' finished.")
            return result
        
        except Exception as e:
            # 5. LOG AFTER (FAILURE)
            logger.error(f"AUDIT: Failed. '{magic_name}' caused error: {e}")
            raise e # Important: Don't hide the error, let it bubble up

    return wrapper

def magic_transaction(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # 1. Start Transaction context
        # (In a real DB, here we would do: db.begin())
        
        try:
            # 2. Execute functionality
            result = func(*args, **kwargs)
            
            # 3. Commit (Save changes)
            # (In a real DB: db.commit())
            return result
            
        except Exception as e:
            # 4. Rollback (Undo changes)
            logger.critical(f"TRANSACTION: Critical error in magic core. Rolling back.")
            # (In a real DB: db.rollback())
            
            # Re-raise the error so the user knows it failed
            raise e
            
    return wrapper

def require_permission(permission_needed: str):
    # LAYER 1: Receives the argument ("cast_offensive")
    
    def decorator(func):
        # LAYER 2: Receives the function (cast_spell)
        
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # LAYER 3: Receives the call arguments (user=Harry)
            
            # A. Get the user from the arguments
            current_user = kwargs.get('user')
            
            if not current_user:
                raise HTTPException(status_code=401, detail="Unauthorized: No user credentials.")

            # B. Check permissions using the User model logic
            # This connects the decorator to your User.py file logic
            if not current_user.has_permission(permission_needed):
                
                # C. If check fails, STOP EVERYTHING.
                logger.warning(f"SECURITY: {current_user.username} denied access to {permission_needed}.")
                raise HTTPException(status_code=403, detail="Forbidden: Insufficient permissions.")

            # D. If check passes, allow the function to run
            return func(*args, **kwargs)
            
        return wrapper
    return decorator