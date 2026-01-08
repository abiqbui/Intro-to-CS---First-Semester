# Name: Abigail Bui
# Period: 7
# Assignment: Week 1 HW - With
# Time Spent: 2 class periods



entries = int(input("How many entries are being entered?"))

with open('step_count_tracker.txt', 'a') as file_var, open('step_count_tracker.txt', 'r') as file_rd:
  for num in range(1, entries + 1):
    entry = input(f'#{num} What would you like to add to the file?')
    file_var.write(f'{entry}\n')
  line = file_rd.readline()
  sum = 0
  while line != "" :
    sum += int(line)
    line = file_rd.readline()    

print(f"You've competed a total of {sum} steps so far!")
