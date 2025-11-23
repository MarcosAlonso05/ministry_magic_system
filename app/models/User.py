from dataclasses import dataclass, field
from app.data.magic_catalog import ROLE_STATS

ROLE_PERMISSIONS = {
    "1_year_student": ["cast_basic"],
    "2_year_student": ["cast_basic", "cast_normal"],
    "3_year_student": ["cast_basic", "cast_normal", "cast_difficult"],
    "4_year_student": ["cast_basic", "cast_normal", "cast_difficult", "cast_advanced"],
    "teacher": ["cast_basic", "cast_normal", "cast_difficult", "cast_advanced", "audit"],
    "admin": ["admin"]
}

@dataclass
class User:
    username: str
    role: str
    max_hp: int = field(init=False)
    current_hp: int = field(init=False)
    max_mana: int = field(init=False)
    current_mana: int = field(init=False)

    def __post_init__(self):
        stats = ROLE_STATS.get(self.role, {"hp": 50, "mana": 10})
        self.max_hp = stats["hp"]
        self.current_hp = stats["hp"]
        self.max_mana = stats["mana"]
        self.current_mana = stats["mana"]

    def has_permission(self, required_permission: str) -> bool:
        my_permissions = ROLE_PERMISSIONS.get(self.role, [])
        if "admin" in my_permissions:
            return True
        return required_permission in my_permissions