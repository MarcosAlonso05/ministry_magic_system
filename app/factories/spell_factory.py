from app.models.Spells import Spell, OffensiveSpell, DefensiveSpell, HealthSpell
from app.data.magic_catalog import SPELL_DATA

class SpellFactory:
    @staticmethod
    def create_spell(spell_name: str) -> Spell:
        key_name = next((k for k in SPELL_DATA.keys() if k.lower() == spell_name.lower()), None)

        if not key_name:
            raise ValueError(f"Spell '{spell_name}' not found in Ministry Grimoire.")

        data = SPELL_DATA[key_name]
        spell_type = data["type"]
        cost = data["cost"]
        perm = data["perm"]

        if spell_type == "offensive":
            return OffensiveSpell(key_name, spell_type, cost, perm)
        elif spell_type == "defensive":
            return DefensiveSpell(key_name, spell_type, cost, perm)
        elif spell_type == "health":
            return HealthSpell(key_name, spell_type, cost, perm)
        else:
            raise ValueError(f"Unknown spell type: {spell_type}")