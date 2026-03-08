# Name: Abigail Bui
# Period: 7
# Assignment: Week 8 HW - Schedule Helper
# Time Spent: 20 min

print('Enter when you are available with a friend so we can see when both of you are free to meet!')

# empty set for person 1's schedule to be added to
schedule1 = set([])

start = input('Are you ready to start? (yes or no): ')

# loops getting different times until the user says they are done

if start == 'yes' or start == 'Yes' or start == 'YES':
    p1time = input('Person 1 -- Please input a time of when you are available to meet (ex. 6:00pm, 4:23pm, 5:00am, etc): ')
    while start == 'yes' or start == 'Yes' or start == 'YES':
        schedule1.add(p1time) # adds time to set
        askp1 = input('Would to like to input another time? (yes or no): ')
        while askp1 == 'yes' or askp1 == 'YES' or askp1 == 'Yes': 
            p1time = input('Time slot (ex. 6:00pm, 4:23pm, 5:00am, etc): ')
            schedule1.add(p1time) # adds time to set
            askp1 = input('Would to like to input another time? (yes or no): ')
        else:
            break
            
print('Time for person 2!')

# empty set for person 2's schedule
schedule2 = set([])

start2 = input('Ready to start? (yes or no): ')

# loops getting different times until the second user is done
if start2 == 'yes' or start2 == 'Yes' or start2 == 'YES':
    p2time = input('Person 2 -- Please input a time of when you are available to meet (ex. 6:00pm, 4:23pm, 5:00am, etc): ')
    while start2 == 'yes' or start2 == 'Yes' or start2 == 'YES':
        schedule2.add(p2time) # adds time to set
        askp2 = input('Would to like to input another time? (yes or no): ')
        while askp2 == 'yes' or askp2 == 'YES' or askp2 == 'Yes': 
            p2time = input('Time slot (ex. 6:00pm, 4:23pm, 5:00am, etc): ')
            schedule2.add(p2time) # adds time to set
            askp2 = input('Would to like to input another time? (yes or no): ')
        else:
            break

# prints list of their overlapping times
print('You guys are both available at: ')
print(schedule1.intersection(schedule2))
