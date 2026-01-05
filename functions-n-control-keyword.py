# Name: Abigail Bui
# Period: 7
# Assignment: Functions & Controlled Keyword Practice
# Time Spent: 10 minutes

# my three functions, each prints a different response

def greeting(): # this function prints the line below
    print("Hello")

def farewell(): # this function prints the line below
    print("Goodbye")
    
def disregarded(): # this function prints the line below
    print("How rude, that was not one of the options.") 

def main():
    enter_exit = input("Enter or exit? ") # asks "enter or exit"
    if enter_exit == "enter":
        greeting() # if user responds "enter" function greeting is called
    elif enter_exit == ("exit"):
        farewell()  # if user responds "farewell" function farewell is called
    else:
        disregarded() # if user responds with anything else function disregarded is called

main() # calls the main function
