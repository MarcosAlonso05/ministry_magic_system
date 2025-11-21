from app.models.Spells import Spell, OffensiveSpell, DefensiveSpell, HealthSpell

class SpellFactory:
    @staticmethod
    def create_spell(spell_name: str) -> Spell:
        
        spell_name = spell_name.title()

        if spell_name == "FireBall":
            return OffensiveSpell("FireBall", "Offensive", 50)
        
        elif spell_name == "Flipendo":
            return OffensiveSpell("Flipendo", "Offensive", 40)

        elif spell_name == "Protego":
            return DefensiveSpell("Protego", "Defensive", 30)
        
        elif spell_name == "Divine":
            return HealthSpell("Divine", "Health", 5)
            
        elif spell_name == "Recover":
            return HealthSpell("Recover", "Health", 10)
        
        else:
            raise ValueError(f"The spell '{spell_name}' is not known in the Ministry database.")