# Name: Abigail Bui
# Period: 7
# Assignment: Creating and Editing Lists HW
# Time Spent: 1 hour 30? 

num_of_val = int(input('How many values do you want to input into your list? ')) # asks how many items your list will have
my_list = [] # empty list to add values to
num = 0 # start count of the value number to be referenced below

while num_of_val > 0:
    num += 1
    val = input(f"Value {num}: ")
    my_list.append(val)
    num_of_val -= 1

print(my_list)

def editing():
    edit_list = input('Would you like to edit the list? (Yes or No) ')
    
    while edit_list == 'yes' or edit_list == 'Yes' or edit_list == 'YES':
        value_num = int(input('What value do you want to edit? (1, 2, 3, 4, etc.) '))
        change = input('What would you like to change this value to? ')
        my_list[value_num-1] = change
        print(my_list)
        edit_list = input('Would you like to edit the list?')
try:
    editing()
except IndexError: 
    print("Try again. You don't have that number value (1, 2, 3, 4, etc.)")
    editing()
