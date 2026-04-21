# Name: Abigail Bui
# Period: 7
# Assignment: Inheritence RPG Character
# Time Spent: 

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
    def take_damage(self, health, damage_taken)
        self.health = self.max_health
        
        print(f"Health is now at {self.health}.")
    def display_stats(self, )