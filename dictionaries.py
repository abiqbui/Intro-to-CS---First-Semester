# Name: Abigail Bui
# Period: 7
# Assignment: Week 7 HW - Dictionaries
# Time Spent: 

birthdays = {}


def adding():
    name = input('Enter the name of person: ')
    date = input('Enter their birthday (month/day): ')
    birthdays[name] = date

def list_people():
    people = input('Would you like to see the people whose birthdays have been added so far? (Yes or no): ')
    if people == 'yes' or people == 'YES' or people == 'Yes':
        print(birthdays.keys())

def list_dates():
    dates = input('Would you like to see the birthdays that have been added so far? (Yes or no): ')
    if dates == 'yes' or dates == 'YES' or dates == 'Yes':
        print(birthdays.values())

def clean_slate():
    clear = input('Would you like to clear all of the prior values inputed? (Yes or no): ')
    if clear == 'yes' or clear == 'YES' or clear == 'Yes':
        birthdays.clear()


add = input('Would you like to add a birthday? (Yes or no): ')

while add == 'yes' or add == 'YES' or add == 'Yes':
    adding()
    add = input('Would you like to add another birthday? (Yes or no): ')
else:
    list_people()
    list_dates()
    clean_slate()