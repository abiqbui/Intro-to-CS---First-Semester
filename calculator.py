# Name: Abigail Bui
# Period: 7
# Assignment: Week 2 HW - Try/Except Records
# Time Spent: 

num_1 = int(input("Enter a number: "))
num_2 = int(input("Enter a number: "))
operation = input("Do you want to add(+), subtract(-), multiply(*) or divide(/)? ")

try:
    if operation == "add" or operation == "Add" or operation == "ADD" or operation == "+" or operation == "(+)":
        result = num_1+num_2
        print(result)
    elif operation == "subtract" or operation == "Subtract" or operation == "SUBTRACT" or operation == "-" or operation == "(-)":
        result = num_1-num_2
        print(result)
    elif operation == "multiply" or operation == "Multiply" or operation == "MULTIPLY" or operation == "*" or operation == "(*)":
        result = num_1*num_2
        print(result)
    elif operation == "divide" or operation == "Divide" or operation == "DIVIDE" or operation == "/" or operation == "(/)":
        result = num_1/num_2
        print(result)
    else:
        print("Please pick one of the four options presented.")
except ZeroDivisionError:
    print("You cannot divide a number by zero. Your answer is undefined.")
except ValueError:
    print("Please enter numbers.")
except:
    print("An error has occurred.")
finally:
    with open("math_record.txt", "a") as math_record:
        