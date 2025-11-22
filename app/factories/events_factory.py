from app.models.MagicEvents import MagicEvents, OffensiveEvents, DefensiveEvents, UtilityEvents
from app.data.magic_catalog import EVENT_DATA

class EventFactory:
    @staticmethod
    def create_event(event_name: str) -> MagicEvents:
        key_name = next((k for k in EVENT_DATA.keys() if k.lower() == event_name.lower()), None)

        if not key_name:
            raise ValueError(f"Event '{event_name}' not found in Ministry Records.")

        data = EVENT_DATA[key_name]
        event_type = data["type"]
        cost = data["cost"]
        perm = data["perm"]

        if event_type == "offensive":
            return OffensiveEvents(key_name, event_type, cost, perm)
        elif event_type == "defensive":
            return DefensiveEvents(key_name, event_type, cost, perm)
        elif event_type == "utility":
            return UtilityEvents(key_name, event_type, cost, perm)
        else:
            raise ValueError(f"Unknown event type: {event_type}")