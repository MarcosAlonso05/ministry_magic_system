SPELL_DATA = {
    # YEAR 1
    "Flipendo": {"type": "offensive", "cost": 10, "perm": "cast_basic", "power": 15},
    "Protego":  {"type": "defensive", "cost": 10, "perm": "cast_basic", "power": 20},
    "Episkey":  {"type": "health",    "cost": 15, "perm": "cast_basic", "power": 20},

    # YEAR 2
    "Incendio":       {"type": "offensive", "cost": 30, "perm": "cast_normal", "power": 35},
    "Salvio Hexia":   {"type": "defensive", "cost": 35, "perm": "cast_normal", "power": 40},
    "Reparifors":     {"type": "health",    "cost": 25, "perm": "cast_normal", "power": 35},

    # YEAR 3
    "Confringo":      {"type": "offensive", "cost": 50, "perm": "cast_difficult", "power": 60},
    "Protego Maxima": {"type": "defensive", "cost": 60, "perm": "cast_difficult", "power": 70},
    "Vulnera Sanentur": {"type": "health",  "cost": 55, "perm": "cast_difficult", "power": 60},

    # YEAR 4
    "Fireball":       {"type": "offensive", "cost": 80, "perm": "cast_advanced", "power": 100},
    "Fianto Duri":    {"type": "defensive", "cost": 90, "perm": "cast_advanced", "power": 100},
    "Panacea":        {"type": "health",    "cost": 100, "perm": "cast_advanced", "power": 100},
}

EVENT_DATA = {
    # YEAR 1
    "Sparks":    {"type": "offensive", "cost": 5,  "perm": "cast_basic", "power": 5},
    "Mist":      {"type": "defensive", "cost": 5,  "perm": "cast_basic", "power": 10},
    "Water":     {"type": "utility",   "cost": 5,  "perm": "cast_basic", "power": 5},

    # YEAR 2
    "RockThrow": {"type": "offensive", "cost": 20, "perm": "cast_normal", "power": 25},
    "TreeWall":  {"type": "defensive", "cost": 20, "perm": "cast_normal", "power": 30},
    "Light":     {"type": "utility",   "cost": 15, "perm": "cast_normal", "power": 15},

    # YEAR 3
    "Tornado":   {"type": "offensive", "cost": 60, "perm": "cast_difficult", "power": 55},
    "EarthDome": {"type": "defensive", "cost": 65, "perm": "cast_difficult", "power": 60},
    "Growth":    {"type": "utility",   "cost": 40, "perm": "cast_difficult", "power": 40},

    # YEAR 4
    "Meteor":    {"type": "offensive", "cost": 120, "perm": "cast_advanced", "power": 150},
    "TimeStop":  {"type": "defensive", "cost": 200, "perm": "cast_advanced", "power": 200},
    "SunBurst":  {"type": "utility",   "cost": 100, "perm": "cast_advanced", "power": 100},
}

ROLE_STATS = {
    "1_year_student": {"hp": 100, "mana": 50},
    "2_year_student": {"hp": 150, "mana": 100},
    "3_year_student": {"hp": 250, "mana": 200},
    "4_year_student": {"hp": 400, "mana": 350},
    "teacher":        {"hp": 800, "mana": 800},
    "admin":          {"hp": 9999, "mana": 9999}, # GOD MODE
}