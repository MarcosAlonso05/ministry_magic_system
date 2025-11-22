from fastapi import Header, HTTPException
from app.models.User import User

users_db = {
    "admin": User(username="admin", role="admin"),
    "harry": User(username="harry", role="1_year_student"),
    "elaina": User(username="elaina", role="4_year_student"),
    "gandalf": User(username="gandalf", role="teacher"),
}

def get_current_user(x_user_id: str = Header(...)) -> User:
    
    user_key = x_user_id.lower() 
    
    user = users_db.get(user_key)
    
    if not user:
        raise HTTPException(status_code=400, detail="User not found in Ministry records")
    
    return user