from abc import ABC, abstractmethod

class Spell(ABC):
    def __init__(self, name: str, spell_type: str, mana_cost: int, required_permission: str):
        self.name = name
        self.spell_type = spell_type
        self.mana_cost = mana_cost
        self.required_permission = required_permission

    @abstractmethod
    def execute(self):
        pass

class OffensiveSpell(Spell):
    def execute(self):
        return f"CASTING OFFENSIVE SPELL: {self.name}! Target takes damage."

class DefensiveSpell(Spell):
    def execute(self):
        return f"CASTING DEFENSIVE SPELL: {self.name}! Shield activated."

class HealthSpell(Spell):
    def execute(self):
        return f"CASTING HEALTH SPELL: {self.name}! Health restored."