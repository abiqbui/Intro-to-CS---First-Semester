# Name: Abigail Bui
# Period: 7
# Assignment: Week 8 HW - Pickle Practice
# Time Spent: 


import pickle

with open('practice.dat', 'wb') as outfile:
    set1 = set([])

    set2 = set([])

    print('Add items to your first list.')

    start1 = 'yes'

    while start1 == 'yes' or start1 == 'Yes' or start1 == 'YES':
        item = input('Enter item: ')
        set1.add(item)
        start1 = input('Would you like to add another item? (yes or no): ')
    else:
        start1 = 'no'

    print('Time for your second list!')

    start2 = 'yes'

    while start2 == 'yes' or start2 == 'Yes' or start2 == 'YES':
        item2 = input('Enter item: ')
        set2.add(item2)
        start2 = input('Would you like to add another item? (yes or no): ')
    else:
        start2 = 'no'

    union = (set1|set2)
    print(union)
    
    pickle.dump(union,outfile)
    print('successful')