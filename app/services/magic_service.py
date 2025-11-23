from app.factories.spell_factory import SpellFactory
from app.factories.events_factory import EventFactory
from app.decorators import audit_log, magic_transaction, validate_magic_permission
from app.models.User import User

class MagicService:

    @magic_transaction
    @audit_log
    @validate_magic_permission
    def execute_magic(self, user: User, magic_name: str, is_event: bool = False):
        
        if is_event:
            magic_object = EventFactory.create_event(magic_name)
        else:
            magic_object = SpellFactory.create_spell(magic_name)
        
        return magic_object.execute()