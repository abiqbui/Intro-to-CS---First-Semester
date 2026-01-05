# Name: Abigail Bui
# Period: 7
# Assignment: F-string Receipt Maker
# Time Spent: 2 hours? Wednesday short class + Thursday class

# Item 1
item1 = input ('Item 1 Name: ')
item1Cost = float (input ('Cost of Item 1:'))

# Item 2
item2 = input ('Item 2 Name: ')
item2Cost = float (input ('Cost of Item 2:'))

# Item 3
item3 = input ('Item 3 Name: ')
item3Cost = float (input ('Cost of Item 3:'))

# Item 4
item4 = input ('Item 4 Name: ')
item4Cost = float (input ('Cost of Item 4:'))

# Item 5
item5 = input ('Item 5 Name: ')
item5Cost = float (input ('Cost of Item 5:'))

# Item 6
item6 = input ('Item 6 Name: ')
item6Cost = float (input ('Cost of Item 6:'))

# Item 7
item7 = input ('Item 7 Name: ')
item7Cost = float (input ('Cost of Item 7:'))

# Item 8
item8 = input ('Item 8 Name: ')
item8Cost = float (input ('Cost of Item 8:'))

# Item 9
item9 = input ('Item 9 Name: ')
item9Cost = float (input ('Cost of Item 9:'))

# Item 10
item10 = input ('Item 10 Name: ')
item10Cost = float (input ('Cost of Item 10:'))

# Sum of all products
total = item1Cost + item2Cost + item3Cost + item4Cost + item5Cost + item6Cost + item7Cost + item8Cost + item9Cost + item10Cost

# Print the full receipt (f-string)

receipt = f"""
   **************************************************
       
   {item1}                               ${item1Cost}
   {item2}                               ${item2Cost}
   {item3}                               ${item3Cost} 
   {item4}                               ${item4Cost} 
   {item5}                               ${item5Cost} 
   {item6}                               ${item6Cost} 
   {item7}                               ${item7Cost} 
   {item8}                               ${item8Cost} 
   {item9}                               ${item9Cost} 
   {item10}                               ${item10Cost} 
       
    Total:                               ${total}
   **************************************************
"""

print (receipt)
