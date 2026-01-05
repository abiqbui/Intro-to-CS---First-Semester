# Name: Abigail Bui
# Period: 7
# Assignment: File I/O Practice
# Time Spent: 40 min

# creating my file in written mode
my_file = open('my_file.txt', 'w') 
# writing my three line
my_file.write("This is line one of my file.\n")
my_file.write("This is line two of my file.\n")
my_file.write("The third line of my file!\n")
# closing the file
my_file.close()

# reopening the file in read mode
my_file = open('my_file.txt', 'r')
# reading individual lines
line_1 = my_file.readline()
line_2 = my_file.readline()
line_3 = my_file.readline()
# closing the file again
my_file.close()

# printing all the lines
print(line_1)
print(line_2)
print(line_3)
