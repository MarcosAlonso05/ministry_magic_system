from app.models.MagicEvents import MagicEvents, OffensiveEvents, DefensiveEvents, UtilityEvents

class EventFactory:
    @staticmethod
    def create_event(event_name: str) -> MagicEvents:
        
        event_name = event_name.title()

        if event_name == "Tornado":
            return OffensiveEvents("Tornado", "Offensive", 50)
        
        elif event_name == "Rock":
            return OffensiveEvents("Rock", "Offensive", 40)

        elif event_name == "Tree":
            return DefensiveEvents("Tree", "Defensive", 30)
        
        elif event_name == "Water":
            return UtilityEvents("Water", "Health", 5)
            
        elif event_name == "Light":
            return UtilityEvents("Light", "Health", 10)
        
        else:
            raise ValueError(f"The event '{event_name}' is not known in the Ministry database.")