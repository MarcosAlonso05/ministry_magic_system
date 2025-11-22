from abc import ABC, abstractmethod

class MagicEvents(ABC):
    def __init__(self, name: str, event_type: str, mana_cost: int, required_permission: str):
        self.name = name
        self.event_type = event_type
        self.mana_cost = mana_cost
        self.required_permission = required_permission

    @abstractmethod
    def execute(self):
        pass

class OffensiveEvents(MagicEvents):
    def execute(self):
        return f"CASTING OFFENSIVE Events: {self.name}! Target takes damage."

class DefensiveEvents(MagicEvents):
    def execute(self):
        return f"CASTING DEFENSIVE Events: {self.name}! Shield activated."

class UtilityEvents(MagicEvents):
    def execute(self):
        return f"CASTING UTILITY Events: {self.name}! Environment changed."