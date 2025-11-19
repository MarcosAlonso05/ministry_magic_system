from app.models.Spells import Spell, OffensiveSpell, DefensiveSpell, UtilitySpell

class SpellFactory:
    @staticmethod
    def create_spell(spell_name: str) -> Spell:
        
        spell_name = spell_name.title()

        if spell_name == "Expelliarmus":
            return OffensiveSpell("Expelliarmus", "Offensive", 50)
        
        elif spell_name == "Stupefy":
            return OffensiveSpell("Stupefy", "Offensive", 40)

        elif spell_name == "Protego":
            return DefensiveSpell("Protego", "Defensive", 30)
        
        elif spell_name == "Lumos":
            return UtilitySpell("Lumos", "Utility", 5)
            
        elif spell_name == "Alohomora":
            return UtilitySpell("Alohomora", "Utility", 10)
        
        else:
            # Default generic spell or error
            raise ValueError(f"The spell '{spell_name}' is not known in the Ministry database.")