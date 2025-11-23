from fastapi import APIRouter, HTTPException, Body
from app.data.database import users_db
from app.models.User import User
from app.data.magic_catalog import SPELL_DATA, EVENT_DATA, ROLE_STATS
from typing import List, Dict

router = APIRouter(prefix="/api", tags=["Frontend API"])

@router.get("/users")
def get_all_users():
    user_list = []
    for u in users_db.values():
        user_list.append({
            "username": u.username, 
            "role": u.role, 
            "hp": u.max_hp, 
            "mana": u.max_mana
        })
    return user_list

@router.post("/users/create")
def create_new_user(user_data: Dict[str, str] = Body(...)):
    raw_username = user_data.get("username", "")
    username = raw_username.strip().lower()
    role = user_data.get("role")

    if not username or not role:
        raise HTTPException(status_code=400, detail="Missing username or role")
    
    if username in users_db:
        raise HTTPException(status_code=400, detail="Wizard name already taken!")
    
    if role == "admin":
        raise HTTPException(status_code=403, detail="Cannot create Admin users via public terminal")

    try:
        new_user = User(username=username, role=role)
        users_db[username] = new_user
        return {"status": "success", "username": username}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/verify-admin")
def verify_admin(password: Dict[str, str] = Body(...)):
    if password.get("password") == "1234":
        return {"status": "success"}
    raise HTTPException(status_code=401, detail="Wrong password")

@router.get("/catalog")
def get_battle_catalog():
    return {
        "spells": SPELL_DATA,
        "events": EVENT_DATA,
        "roles_stats": ROLE_STATS
    }