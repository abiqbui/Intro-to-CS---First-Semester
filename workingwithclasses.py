# Name: Abigail Bui
# Period: 7
# Assignment: Week 11 HW - Working With Classes
# Time Spent: 30 min

from orchard import FruitTree

tree1 = FruitTree('1', '10', 'good', 'apple', '15 bushels')
tree2 = FruitTree('2', '10', 'poor', 'orange', '200 oranges')
tree3 = FruitTree('3', '10', 'excellent', 'peach', '6 bushels')

orchard_trees = [tree1, tree2, tree3]

# checking health of the trees
checking_health = input("Would you like to check the health of your trees? (Y or N): ")

if checking_health == "Y":
    for tree in orchard_trees:
        print(tree.check_health())
    print()

# checking expected yield of the trees
checking_yield = input("Would you like to check the expected yield of your trees? (Y or N): ")
if checking_yield == "Y":
    for tree in orchard_trees:
        print(tree.check_yield())

