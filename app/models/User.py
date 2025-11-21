from dataclasses import dataclass, field

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
    
    def has_permission(self, required_permission: str) -> bool:
        my_permissions = ROLE_PERMISSIONS.get(self.role, [])

        if "admin" in my_permissions:
            return True

        return required_permission in my_permissions
