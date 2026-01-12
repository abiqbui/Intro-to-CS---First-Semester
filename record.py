
marker = 'y'

num_records = int(input('How many records do you want to create? ')) # get number of records

with open('records.txt','w') as record_file: # Open file for writing
  while marker == 'y' or marker == 'Y':
    for count in range(1, num_records + 1):
       print(f'Enter data for record #{count}')
    # get fields for a record
       field_1 = input('Field 1: ')
       field_2 = input('Field 2: ')
       field_3 = input('Field 3: ')
       record_file.write(f'{field_1}\n') # write record to file
       record_file.write(f'{field_2}\n')
       record_file.write(f'{field_3}\n')
    marker = input('Enter Y if you wish to continue. Otherwise enter N.')
print() # prints a blank line
print('Records have been written to records.txt')
print() # prints a blank line

with open('records.txt','r') as record_file:
  field_1 = record_file.readline()
  while field_1 != '':
    field_2 = int(record_file.readline())
    field_3 = float(record_file.readline())
    field_1 = field_1.rstrip('\n')
    print(f'Field 1: {field_1}')
    print(f'Field 2: {field_2}')
    print(f'Field 3: {field_3}')
    field_1 = record_file.readline()
