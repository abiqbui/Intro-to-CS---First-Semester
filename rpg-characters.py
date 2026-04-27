# Name: Abigail Bui
# Period: 7
# Assignment: Inheritence RPG Character
# Time Spent: 2 hours?

class RPG_Character:
    def __init__(self, name, max_health, attack_power, level):
        self.name = name
        self.max_health = max_health
        self.attack_power = attack_power
        self.level = level
    def attack(self, type, damage_dealt):
        self.type = type
        self.damage_dealt = damage_dealt
        print(f"{self.name} uses {self.type}. Enemy takes {self.damage_dealt} damage.")
    def take_damage(self, damage_taken):
        self.health = self.max_health
        self.damage_taken = damage_taken
        new_health = self.health - self.damage_taken
        print(f"Health is now at {new_health}.")
    def display_stats(self):
        print(f"Name: {self.name}  Max Health: {self.max_health}  Attack Power: {self.attack_power}  Level: {self.level}")

class Healer (RPG_Character):
    def __init__(self, name, max_health, attack_power, level, magic_type):
        RPG_Character.__init__(self, name, max_health, attack_power, level)
        self.magic_type = magic_type
    def take_damage(self, damage_taken):
        self.health = self.max_health
        self.damage_taken = damage_taken/2
        new_health = self.health - self.damage_taken
        print(f"Health is now at {new_health}.")
    def self_heal(self):
        self.health = self.max_health
        print(f"Health is now at {self.max_health}. Max health!")
    def heal_ally(self, ally_name, ally_health, ally_damage):
        self.ally_name = ally_name
        self.ally_damage = ally_damage
        self.ally_health = ally_health
        heal_health = self.ally_health + (self.ally_damage/2)
        print(f"{self.ally_name}'s health has regenerated to {heal_health}")

class Support (RPG_Character):
    def __init__(self, name, max_health, attack_power, level, magic_type):
        RPG_Character.__init__(self, name, max_health, attack_power, level)
        self.magic_type = magic_type
    def display_stats(self, durability):
        self.durability = durability
        print(f"Name: {self.name}  Max Health: {self.max_health}  Attack Power: {self.attack_power}  Level: {self.level}  Durability: {self.durability}/10")
    def shield(self):
        damage_absorbed = self.damage_taken * (self.durability/10)
        percentage = self.durability * 10
        self.damage_taken = self.damage_taken - self.durability
        print(f"Shield absorbs {percentage}% of the damage.")
