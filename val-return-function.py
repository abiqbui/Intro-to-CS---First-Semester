# Name: Abigail Bui
# Period: 7
# Assignment: Value Return Function HW
# Time Spent: 20 min


def math(num1, num2): # function with 2 parameters
    # the four primary mathematical operations using the parameters
    minus = num1 - num2
    add = num1 + num2
    divide = num1 / num2
    multiply = num1 * num2
    # printing each operation 
    print(f"Subtraction: {num1} - {num2} = {minus}")
    print(f"Addition: {num1} + {num2} = {add}")
    print(f"Division: {num1} / {num2} = {divide}")
    print(f"Multiplication: {num1} * {num2} = {multiply}")
    # returning the 4 different operations using the 2 parameters
    return minus, add, divide, multiply
    
# calling the function with different parameters each time
# each time prints different values because the parameters are different
math(10, 2) 
math(5, 6)
math(7,8)
