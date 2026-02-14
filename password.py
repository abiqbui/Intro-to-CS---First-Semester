# Name: Abigail Bui
# Period: Period 7
# Assignment: Password Checker
# Time Spent: an hourish?


def password():

    good_password = ''

    # getting all the requirements

    print('Input your password requirements!')
    print()

    # uppercase letter requirement
    uppercase = int(input('Minimum # of uppercase letters: ')) 
    print()

    # special character requirement
    special = int(input('Minimum # of special characters: '))
    print()

    # number requirement
    numbers = int(input('Minimum # of numbers: '))
    print()

    # length minimum requirement
    minimum = int(input('Minimum length of your password (must be at least your last three answers combined): '))

    print()

    # making sure the minimum is reasonable

    smallest_min = uppercase + special + numbers
    # makes sure the minimum isn't less than all the requirements added
    if minimum < smallest_min: 
        print(f'Your minimum must be at least {smallest_min}.')
        # asks for a reasonable minimum
        minimum = int(input(f'Minimum length of your password (must be at least {smallest_min}): '))
    print()

    # length maximum requirement
    maximum = int(input('Maximum length of your password: '))
    print()

    # getting the user-made password
    password = input('Make your password: ')
    print()


    # making sure the password meets the length requirements

    if len(password) < minimum:
        # if the length is below the minimum -> bad password + alerts user
        print('Your password is too short.')
        good_password = 'no'

    elif len(password) > maximum:
        # if the length is above the maximum -> bad password + alerts user
        print('Your password is too long.')
        good_password = 'no'


    # making sure the password meets the special character requirement

    special_chars = 0

    for ch in password:
        # checks ever character to see if it is a special character
        # if so it adds it to the count to compare below
        if ch.isalnum() == False:
            special_chars += 1

    if special_chars < special:
        # if the number of special characters in the password is below the requirement -> bad password + alerts user
        print(f'You need a minimum of {special} special character(s).')
        good_password = 'no'


    # making sure the password meets the uppercase letters requirement

    uppercase_letters = 0

    for ch in password:
        # checks ever character to see if it is an uppercase letter
        # if so it adds it to the count to compare below
        if ch.isupper() == True:
            uppercase_letters += 1

    if uppercase_letters < uppercase:
        # if the number of uppercase letters in the password is below the requirement -> bad password + alerts user
        print(f'You need at least {uppercase} uppercase letter(s).')
        good_password =  'no'


    # making sure the password meets the number(s) requirement

    number_count = 0

    for ch in password:
        # checks ever character to see if it is a number
        # if so it adds it to the count to compare below
        if ch.isdigit() == True:
            number_count += 1

    if number_count < numbers:
        # if the number of numbers in the password is below the requirement -> bad password + alerts user
        print(f'You need at least {numbers} number(s).')
        good_password = 'no'

    # final consensus if the password is good (meets all the requirements)

    if good_password == 'no':
        print('Your password is not a good password. It does not meet 1 or more of the requirements.')
    else:
        # changes value of good_password to 'yes' to use in the file
        good_password = 'yes'
        print('Great password!')

    
    # adding everything to a record
    
    with open('passwords.txt', 'a') as password_records:
        password_records.write(f'Minimum # of uppercase letters: {uppercase}\n')
        password_records.write(f'Minimum # of special characters: {special}\n')
        password_records.write(f'Minimum # of numbers: {numbers}\n')
        password_records.write(f'Minimum length of your password: {minimum}\n')
        password_records.write(f'Maximum length of your password: {maximum}\n')
        password_records.write(f'Password: {password}\n')
        password_records.write(f'Met all of requirements: {good_password}\n')
        password_records.write(f'\n') # blank space to make file easier to read



def main():
    # asks if you want to make a password
    question = input('Would you like to make a password? (Yes or no): ')
    print()
    while question == 'Yes' or question == 'yes' or question == 'YES':
        # if yes then everything above is executed + asks again to maintain loop/add more passwords and requirement to the file
        password()
        print()
        question = input('Would you like to make another password? (Yes or no): ')


main()