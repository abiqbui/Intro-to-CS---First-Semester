# Name: Abigail Bui
# Period: 7
# Assignment: Week 15 HW - Fibonacci
# Time Spent: 30 min


def Fib(n):

    if n == 1:
        return 0
    
    if n == 2:
        return 1
    
    return Fib(n-1)+Fib(n-2)

n_input = int(input("Input # of fibonacci sequence numbers you would like to see: "))

for i in range(1, n_input):
    print(Fib(i))