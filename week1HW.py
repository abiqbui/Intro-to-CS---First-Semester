# Name: Abigail Bui
# Period: 3
# Assignment: Input, Output, Variables, & Arrays
# Time Spent: 5 min

ready = input("Let's to basic math. Ready? (Y or N): ")

equations = []
answers = []

while ready == "Y":

    num1 = int(input("Input a number: "))
    num2 = int(input("Input another number: "))

    method = input("Would you like to add(+), subtract(-), multiply(*), or divide(/): ")

    

    if method == "add" or method == "+":
        sum = num1+num2
        equations.append(f"{num1}+{num2}")
        answers.append(sum)
        print(f"{num1}+{num2}={sum}")
    elif method == "minus" or method == "-":
        difference = num1-num2
        equations.append(f"{num1}-{num2}")
        answers.append(difference)
        print(f"{num1}-{num2}={difference}")
    elif method == "multiply" or method == "*":
        product = num1*num2
        equations.append(f"{num1}*{num2}")
        answers.append(product)
        print(f"{num1}*{num2}={product}")
    elif method == "divide" or method == "/":
        quotient = num1/num2
        equations.append(f"{num1}/{num2}")
        answers.append(quotient)
        print(f"{num1}/{num2}={quotient}")


    ask_e = input("Would you like to look at all equations inputted? (Y or N): ")

    if ask_e == 'Y':
        print(equations)

    ask_a = input("Would you like to look at all answers given? (Y or N): ")

    if ask_a == 'Y':
        print(answers)