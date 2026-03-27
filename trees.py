# Name: Abigail Bui
# Period: 7
# Assignment: Week 11 HW - Working With Classes
# Time Spent: 

# these are my classes to import to another file

class Tree:
    def __init__(self, tree_id, age, health):
        self.tree_id = tree_id
        self.age = age
        self.health = health
    def check_health(self):
        return f"Tree {self.tree_id} is in {self.health} condition."

class FruitTree(Tree):
    def __init__(self, tree_id, age, health, fruit, expected_yield):
        super().__init__(tree_id, age, health)
        self.fruit = fruit
        self.expected_yield = expected_yield
    def check_yield(self):
        return f"The {self.fruit} tree, Tree {tree_id}, is expeced to yield {self.expected_yield} fruit this year."
    
class AppleTree(FruitTree):
    def __init__(self, tree_id, age, health, fruit, expected_yield, type, season):
        super().__init__(tree_id, age, health, fruit, expected_yield)
        self.fruit = 'apples'
        self.type = type
        self.season = season
    def get_harvesting_season(self):
        return f"The {self.type} {self.fruit} are best to harvest in {self.season}."
    
class OrangeTree(FruitTree):
    def __init__(self, tree_id, age, health, fruit, expected_yield, type, season):
        super().__init__(tree_id, age, health, fruit, expected_yield)
        self.fruit = 'oranges'
        self.type = type
        self.season = season
    def get_harvesting_season(self):
        return f"The {self.type} {self.fruit} are best to harvest in {self.season}."