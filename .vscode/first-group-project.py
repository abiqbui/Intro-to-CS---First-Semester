# Name: Abigail Bui, Valerie Vang, Jaxson Boardman, Shane Cardoza
# Period: 7
# Assignment: Week 5 Group Homework - String Methods
# Time Spent: 

# our code needs to include isalnum and isspace

# An new social media platform is having issues with users making their usernames blank spaces. 
# It is causing problems with other functions of the app. 
# We want to make sure that people aren't using all spaces and aren't using special characters so the app runs properly. 



enter = input('Would you like to make an account? (Yes or no): ')

while enter == 'Yes' or enter == 'YES' or enter == 'yes':
    username = input('Enter a username: ')

    if username.isspace() == True and username.isalnum() == False: # if the username is only spaces then..
        print("Your username cannot be only spaces. Please pick a new username.")
        continue
    else:
        print('Valid Password!')
        break

