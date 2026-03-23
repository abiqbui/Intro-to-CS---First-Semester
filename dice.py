# Name: Abigail Bui
# Period: 7
# Assignment: Week 10 HW - Dice
# Time Spent: one hour?

import random


class D4:
    def __init__(self): # sets the number of sides
        self.sides = 4
    def roll(self): # gets a random number between 1 and the number of sides
        return random.randint(1, self.sides)

# repeats process but with six sides
class D6:
    def __init__(self):
        self.sides = 6
    def roll(self):
        return random.randint(1, self.sides)

# with 8 sides
class D8:
    def __init__(self):
        self.sides = 8
    def roll(self):
        return random.randint(1, self.sides)

# with 10 sides
class D10:
    def __init__(self):
        self.sides = 10
    def roll(self):
        return random.randint(1, self.sides)

# with 12 sides
class D12:
    def __init__(self):
        self.sides = 12
    def roll(self):
        return random.randint(1, self.sides)

# with 20 sides
class D20:
    def __init__(self):
        self.sides = 20
    def roll(self):
        return random.randint(1, self.sides)

# with 100 sides
class D100:
    def __init__(self):
        self.sides = 100
    def roll(self):
        return random.randint(1, self.sides)


def main():
    # making all the classes/different die into variables to use
    die4 = D4()
    die6 = D6()
    die8 = D8()
    die10 = D10()
    die12 = D12()
    die20 = D20()
    die100 = D100()

    pick = input("Which die would you like to roll (4, 6, 8, 10, 12, 20, 100, or ALL): ")

    getting_outcomes = "Y"

    while getting_outcomes == 'Y':
        if pick == '4': # prints results of the four-sided die
            result = die4.roll()
            print("Rolling...")
            print(f"You rolled: {result}")
            break
        elif pick == '6': # prints results of the six-sided die
            result = die6.roll()
            print("Rolling...")
            print(f"You rolled: {result}")
            break
        elif pick == '8': # prints results of the eight-sided die
            result = die8.roll()
            print("Rolling...")
            print(f"You rolled: {result}")
            break
        elif pick == '10': # prints results of the ten-sided die
            result = die10.roll()
            print("Rolling...")
            print(f"You rolled: {result}")
            break
        elif pick == '12': # prints results of the twelve-sided die
            result = die12.roll()
            print("Rolling...")
            print(f"You rolled: {result}")
            break
        elif pick == '20': # prints results of the twenty-sided die
            result = die20.roll()
            print("Rolling...")
            print(f"You rolled: {result}")
            break
        elif pick == '100': # prints results of the hundred-sided die
            result = die100.roll()
            print("Rolling...")
            print(f"You rolled: {result}")
            break
        elif pick == "ALL": # prints results of all the dice
            print("Rolling...")
            print(f"D4: {die4.roll()}")
            print(f"D6: {die6.roll()}")
            print(f"D8: {die8.roll()}")
            print(f"D10: {die10.roll()}")
            print(f"D12: {die12.roll()}")
            print(f"D20: {die20.roll()}")
            print(f"D100: {die100.roll()}")
            break
        else: # loops again if they don't pick one of the provided options
            print("That was not one of the provided options, try again.")
            pick = input("Which die would you like to roll (4, 6, 8, 10, 12, 20, 100, or ALL): ")
            
        
    
main()
