from fastapi import APIRouter, Depends, HTTPException
from app.models.User import User
from app.data.database import get_current_user
from app.services.magic_service import MagicService

router = APIRouter()
service = MagicService()

@router.post("/cast")
def cast_spell_endpoint(
    spell_name: str, 
    is_event: bool = False, 
    current_user: User = Depends(get_current_user)
):
    try:
        result = service.execute_magic(
            user=current_user, 
            magic_name=spell_name, 
            is_event=is_event
        )
        return {"status": "success", "result": result}
        
    except Exception as e:
        raise e