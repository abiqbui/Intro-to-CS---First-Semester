# Name: Abigail Bui
# Period: 3
# Assignment: File Interaction
# Time Spent: 10 min

ask = input("Would you like to make a note? (yes or no): ")

if ask == 'yes' or ask == 'Yes' or ask == 'YES':
    note = input("Note: ")
    with open("notes.txt", "a") as n:
        n.write(f"{note} \n")

look = input("Would you like to look at your note(s)? (yes or no): ")

if look == 'yes' or look == 'Yes' or look == 'YES':
    with open("notes.txt", "r") as n:
        for line in n:
            print(line)