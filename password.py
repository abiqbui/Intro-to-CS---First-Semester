# Name: Abigail Bui
# Period: Period 7
# Assignment: Password Checker
# Time Spent: 


# EC 2pts: Store each password and its complexity requirements as a record

good_password = ''

# getting all the requirements

print('Input your password requirements!')
print()

uppercase = int(input('Minimum # of uppercase letters: '))

print()

special = int(input('Minimum # of special characters: '))

print()

numbers = int(input('Minimum of how many numbers must be in your password? '))

print()

minimum = int(input('What is the minimum length of your password? (Must be at least your last three answers combined) '))

print()

# making sure the minimum is reasonable

smallest_min = uppercase + special + numbers

if minimum < smallest_min:
    print(f'Your minimum must be at least {smallest_min}.')
    minimum = int(input(f'What is the minimum length of your password? (Must be at least {smallest_min}) '))

print()

maximum = int(input('What is the maximum length of your password? '))

print()

# getting the user-made password

password = input('Make your password: ')

print()


# making sure the password meets the length requirements

if len(password) < minimum:
    print('Your password is too short.')
    good_password = 'no'

elif len(password) > maximum:
    print('Your password is too long.')
    good_password = 'no'


# making sure the password meets the special character requirement

special_chars = 0

for ch in password:
    if ch.isalnum() == False:
        special_chars += 1

if special_chars < special:
    print(f'You need a minimum of {special} special character(s).')
    good_password = 'no'


# making sure the password meets the uppercase letters requirement

uppercase_letters = 0

for ch in password:
    if ch.isupper() == True:
        uppercase_letters += 1

if uppercase_letters < uppercase:
    print(f'You need at least {uppercase} uppercase letter(s).')
    good_password =  'no'


# making sure the password meets the number(s) requirement

number_count = 0

for ch in password:
    if ch.isdigit() == True:
        number_count += 1

if number_count < numbers:
    print(f'You need at least {numbers} number(s).')
    good_password = 'no'

# final consensus if the password is good (meets all the requirements)

if good_password == 'no':
    print('Your password is not a good password. It does not meet 1 or more of the requirements.')
else:
    print('Great password!')
    