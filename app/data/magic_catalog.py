SPELL_DATA = {
    # YEAR 1 (cast_basic)
    "Flipendo": {"type": "offensive", "cost": 10, "perm": "cast_basic"},
    "Protego":  {"type": "defensive", "cost": 10, "perm": "cast_basic"},
    "Episkey":  {"type": "health",    "cost": 15, "perm": "cast_basic"},

    # YEAR 2 (cast_normal)
    "Incendio":       {"type": "offensive", "cost": 30, "perm": "cast_normal"},
    "Salvio Hexia":   {"type": "defensive", "cost": 35, "perm": "cast_normal"},
    "Reparifors":     {"type": "health",    "cost": 25, "perm": "cast_normal"},

    # YEAR 3 (cast_difficult)
    "Confringo":      {"type": "offensive", "cost": 50, "perm": "cast_difficult"},
    "Protego Maxima": {"type": "defensive", "cost": 60, "perm": "cast_difficult"},
    "Vulnera Sanentur": {"type": "health",  "cost": 55, "perm": "cast_difficult"},

    # YEAR 4 (cast_advanced)
    "Fireball":       {"type": "offensive", "cost": 80, "perm": "cast_advanced"},
    "Fianto Duri":    {"type": "defensive", "cost": 90, "perm": "cast_advanced"},
    "Panacea":        {"type": "health",    "cost": 100, "perm": "cast_advanced"},
}

EVENT_DATA = {
    # YEAR 1 (cast_basic)
    "Sparks":    {"type": "offensive", "cost": 5,  "perm": "cast_basic"},
    "Mist":      {"type": "defensive", "cost": 5,  "perm": "cast_basic"},
    "Water":     {"type": "utility",   "cost": 5,  "perm": "cast_basic"},

    # YEAR 2 (cast_normal)
    "RockThrow": {"type": "offensive", "cost": 20, "perm": "cast_normal"},
    "TreeWall":  {"type": "defensive", "cost": 20, "perm": "cast_normal"},
    "Light":     {"type": "utility",   "cost": 15, "perm": "cast_normal"},

    # YEAR 3 (cast_difficult)
    "Tornado":   {"type": "offensive", "cost": 60, "perm": "cast_difficult"},
    "EarthDome": {"type": "defensive", "cost": 65, "perm": "cast_difficult"},
    "Growth":    {"type": "utility",   "cost": 40, "perm": "cast_difficult"},

    # YEAR 4 (cast_advanced)
    "Meteor":    {"type": "offensive", "cost": 120, "perm": "cast_advanced"},
    "TimeStop":  {"type": "defensive", "cost": 200, "perm": "cast_advanced"},
    "SunBurst":  {"type": "utility",   "cost": 100, "perm": "cast_advanced"},
}