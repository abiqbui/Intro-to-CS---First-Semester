# Name: Abigail Bui
# Period: 7
# Assignment: Week 2 HW - Try/Except Records
# Time Spent: 2 class periods




try:
    num_1 = int(input("Enter a number: "))
    num_2 = int(input("Enter a number: "))
    operation = input("Do you want to add(+), subtract(-), multiply(*) or divide(/)? ")
    result = ""
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
        print("Please pick one of the four options presented. Try again.")
except ValueError:
    print("Please enter numbers. Try again.")
except ZeroDivisionError:
    print("You cannot divide a number by zero. Your answer is undefined. Try again.")
except:
    print("An error has occurred. Try again.")
else:
    with open("math_record.txt", "w") as math_record:
        math_record.write(f'{operation}\n')
        math_record.write(f'{num_1}\n')
        math_record.write(f'{num_2}\n')
        math_record.write(f'{result}\n')
        print()
        print('Your calculations have been recorded in math_record.txt')


