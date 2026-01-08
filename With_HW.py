# Name: Abigail Bui
# Period: 7
# Assignment: Week 1 HW - With
# Time Spent: 


entries = int(input("How many entries are being entered?"))

with open('step_count_tracker.txt', 'a') as stepfile:
  for num in range(1, entries + 1):
    entry = input(f'#{num} What would you like to add to the file?')
    stepfile.write(f'{entry}\n')


with open('step_count_tracker.txt', 'r') as stepfile:
  line = stepfile.readline()
  sum = 0
  while line != "" :
    sum += int(line)
    line = stepfile.readline()

print(f"You've competed a total of {sum} steps so far!")