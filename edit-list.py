# Name: Abigail Bui
# Period: 7
# Assignment: Creating and Editing Lists HW
# Time Spent: 1 hour 30? 

num_of_val = int(input('How many values do you want to input into your list? ')) # asks how many items your list will have
my_list = [] # empty list to add values to
num = 0 # start count of the value number to be referenced below

while num_of_val > 0:
    num += 1 # adds 1 for each loop so user inputs the next # value
    val = input(f"Value {num}: ") # input of what the value user is adding is
    my_list.append(val) # appends list above and adds value to list
    num_of_val -= 1 # decreases the number of values you're inputing so the loop comes to an end eventually

print(my_list) # print list

def editing(): # editing the list
    edit_list = input('Would you like to edit the list? (Yes or No) ') # first asks if user wants to edit list
    
    while edit_list == 'yes' or edit_list == 'Yes' or edit_list == 'YES': # executes if user wants to edit list
        value_num = int(input('What value do you want to edit? (1, 2, 3, 4, etc.) ')) # asks what index number/value user wants to edit
        change = input('What would you like to change this value to? ') # asks what they want to change the value to 
        my_list[value_num-1] = change # changes index item they chose to what they said they wanted to change it to
        print(my_list) # prints list again with the changes made
        edit_list = input('Would you like to edit the list? (Yes or No) ') # asks if user wants to edit list again (will complete this loop again if yes)

try:
    editing() # executed the editing function (lets user edit list)
except IndexError: # corrects user if they go beyond the index and loops back to executing editing function so they can try again
    print('You do not have that value. Try again (1, 2, 3, 4, etc).')
    editing()