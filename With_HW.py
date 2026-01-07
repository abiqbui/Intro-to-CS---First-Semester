
entries = int("How many entries are being entered?")

step-file = open('step_count_tracker.txt', 'w')

for num in range(1, entries + 1):
  entry = input('#{num} What would you like to add to the file?')
  step-file.write(f'{entry}\n')
step-file.close()
