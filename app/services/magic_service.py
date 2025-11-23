import asyncio
import random
from app.factories.spell_factory import SpellFactory
from app.factories.events_factory import EventFactory
from app.decorators import audit_log, magic_transaction, validate_magic_permission
from app.models.User import User

class MagicService:

    @magic_transaction
    @audit_log
    @validate_magic_permission
    async def execute_magic(self, user: User, magic_name: str, is_event: bool = False): # Nota el 'async'
        
        casting_time = random.uniform(1.0, 3.0)
        await asyncio.sleep(casting_time) 
        
        if is_event:
            magic_object = EventFactory.create_event(magic_name)
        else:
            magic_object = SpellFactory.create_spell(magic_name)
        
        result = magic_object.execute()
        
        return f"{result} (Casting Time: {casting_time:.2f}s)"