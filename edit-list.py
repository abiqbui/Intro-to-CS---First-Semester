# Name: Abigail Bui
# Period: 7
# Assignment: Creating and Editing Lists HW
# Time Spent: 

num_of_val = int(input('How many values do you want to input into your list?'))
my_list = []
num = 0 

while num_of_val > 0:
    num += 1
    val = input(f"Value {num}: ")
    my_list.append(val)
    num_of_val -= 1

print(my_list)

edit_list = input('Would you like to edit the list?')
if edit_list = 'yes' or edit_list = 'Yes' or edit_list = 'YES':
    