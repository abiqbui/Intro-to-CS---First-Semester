# Name: Abigail Bui
# Period: 7
# Assignment: With HW
# Time Spent: 


entries = int("How many entries are being entered?")

step-file = open('step_count_tracker.txt', 'w')

for num in range(1, entries + 1):
  entry = input('#{num} What would you like to add to the file?')
  step-file.write(f'{entry}\n')
step-file.close()


step-file = open('step_count_tracker.txt', 'r')
line = step-list.readline()
sum = 0

while line = !'' :
  sum += int(line)
  line = step-file.readline()
  
step-file.close()
print(f'There are {sum} total entries')
