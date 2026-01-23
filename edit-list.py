# Name: Abigail Bui
# Period: 7
# Assignment: Creating and Editing Lists HW
# Time Spent: 1 hour 30? 

num_of_val = int(input('How many values do you want to input into your list? ')) # asks how many items your list will have
my_list = [] # empty list to add values to
num = 0 # start count of the value number to be referenced below

while num_of_val > 0: 
    num += 1
    val = input(f"Value {num}: ") # gets values
    my_list.append(val) # adds your value input to the list
    num_of_val -= 1 # subtracts 1 for num of val so the loop ends when you've inputed all your values

print(my_list)

def editing():
    edit_list = input('Would you like to edit the list? (Yes or No) ') # asks to edit list
    
    while edit_list == 'yes' or edit_list == 'Yes' or edit_list == 'YES': # if user wants to edit list execute this loop
        value_num = int(input('What value do you want to edit? (1, 2, 3, 4, etc.) ')) # get index number of what value to edit
        change = input('What would you like to change this value to? ') # get the new value
        my_list[value_num-1] = change # change old value to new value
        print(my_list) # print list with new changes
        edit_list = input('Would you like to edit the list? ') # start loop again if they want to edit more
try:
    editing() # calls the editing function
except IndexError: 
    print("Try again. You don't have that number value (1, 2, 3, 4, etc.)")
    editing() # calls the editing function again so they can try again
