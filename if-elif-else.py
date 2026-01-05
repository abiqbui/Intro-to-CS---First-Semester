# Name: Abigail Bui
# Period: 7
# Assignment: if-elif-else HW
# Time Spent: 15 - 20 min?

# assigned secret number value

secret_num = 8


# input their guess

guess = float (input ("Guess a number between 1 - 100: "))


# if-elif-else code

if guess > 100: 
    # if the guess is over 100 it will remind the user of the instructions
    print ("The instructions were between 1 and 100.")
elif guess <= 0: 
    # if the guess is equal to or less than 0 it will remind the user of the instructions
    print ("The instructions were between 1 and 100.")
elif guess > secret_num: 
    # if the guess is greater than the secret number it will tell the user the guess is too high
    print ("Too high")
elif guess < secret_num:
    # if the guess is less than the secret number it will tell the user the guess is too low
    print ("Too low")
else:
    # if the guess is the same as the secret number it will tell the user they got it right
    print ("You got it!")
