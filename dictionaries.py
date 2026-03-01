# Name: Abigail Bui
# Period: 7
# Assignment: Week 7 HW - Dictionaries
# Time Spent: 30 min

birthdays = {}

def adding(): # adds a new key-value to the dictionary using user input
    name = input('Enter the name of person: ')
    date = input('Enter their birthday (month/day): ')
    birthdays[name] = date

def list_people(): # prints all the names inputed
    people = input('Would you like to see the people whose birthdays have been added so far? (Yes or no): ')
    if people == 'yes' or people == 'YES' or people == 'Yes':
        print(birthdays.keys())

def list_dates(): # prints all of the birthdays inputed
    dates = input('Would you like to see the birthdays that have been added so far? (Yes or no): ')
    if dates == 'yes' or dates == 'YES' or dates == 'Yes':
        print(birthdays.values())

def clean_slate(): # empties the list completely
    clear = input('Would you like to clear all of the prior values inputed? (Yes or no): ')
    if clear == 'yes' or clear == 'YES' or clear == 'Yes':
        birthdays.clear()

# loops so user can continue to add birthdays, look at people and dates added, and clear list

birthday_dictionary = input('Would you like to make a list of birthdays? (Yes or no): ')

while birthday_dictionary == 'yes' or birthday_dictionary == 'Yes' or birthday_dictionary == 'YES':
    add = input('Would you like to add a birthday? (Yes or no): ')

    while add == 'yes' or add == 'YES' or add == 'Yes':
        adding()
        add = input('Would you like to add another birthday? (Yes or no): ')
    else:
        list_people()
        list_dates()
        clean_slate()

        while add == 'yes' or add == 'YES' or add == 'Yes':
            adding()
            add = input('Would you like to add another birthday? (Yes or no): ')
        else:
            list_people()
            list_dates()
            clean_slate()
        
        print()
        # ends loop when user is done inputing values
        birthday_dictionary = input('Would you like to continue adding? (Yes or no): ')
