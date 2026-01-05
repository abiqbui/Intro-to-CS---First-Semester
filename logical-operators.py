# Name: Abigail Bui
# Period: 7
# Assignment: Logical Operators Practice HW
# Time Spent: 30 min?


print ("Please submit your answers in all lowercase ")

# or 

animal = str(input("What type of animal is a leopard? ")) 

if animal == "mammal" or animal == "felidae" or animal == "feline":
    print ("Correct!") 
    # if the user says a leopard is a mammal, a felidae, or a feline, then the code will say they are correct
else:
    print ("Actually, leopards are mammals and part of the felidae/feline family! ")
    # if the user's answer is anything besides mammal, felidae, or feline, it will correct the user

# and

number = float (input("There are _______ wild leopards in the world: "))

if number >= 240000 and number <= 250000:
    print ("Pretty close! Its estimated that there are fewer than 250000 wild leopards.")
    # if the number the user inputs is between 240000 and 250000 then the code will confirm they are within the range
else:
    print("Not quite. Its estimated that there are fewer than 250000 wild leopards.")
    # if the number the user inputs is not within the range the code will correct them

# not 

dots = str (input("What is the correct term for a leopard's dots? "))

if not (dots == "rosettes"):
    print ("Incorrect. The correct term is rosettes")
    # if the answer the user inputs is anything other than "rosettes" than the code will correct them
else: 
    print ("Correct! Isn't that such a pretty name?")
    # if the answer is rosettes the code will confirm they are right
    
# combo

if (number >= 240000 and number <= 250000) and (animal == "mammal" or animal == "felidae" or animal == "feline") and (dots == "rosettes"):
    print("Wow you really know a lot about leopards don't you?") 
    # if the user got all the previous questions correct, the code will commend their knowledge of leopards
else: 
    print ("Leopards are really cool!")
    # if the user did not get all of the previous questions correct, the code will just state that leopards are cool
