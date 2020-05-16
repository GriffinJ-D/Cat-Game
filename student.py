class Cat:
    def __init__(self, name, level, weight, attack, health, speed, current_health, XP):
        self.name = name
        self.level = level
        self.weight = weight
        self.attack = attack
        self.health = health
        self.speed = speed
        self.current_health = current_health
        self.XP = XP

class Attack:
    def __init__(self, name, power):
        self.name = name
        self.power = power

class Bird:
    def __init__(self, level, weight, speed, XP):
        self.level = level
        self.weight = weight
        self.speed = speed
        self.XP = XP
