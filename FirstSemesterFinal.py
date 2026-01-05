# Name: Abigail Bui
# Period: 7
# Project Name: My Book Diary
# Time Spent: 3 days

# Project Description:
# This program is my *book diary*. It will give me something to turn back to if I want to see what books I've read. 
# I will be able to add the title, author, page count, and genre(s) of the book. I will also be able to input my rating of the book. 
# The books will be ordered by the order in which they were input and I will be able to look back at them whenever I wish

import csv 

def make_file(): # make file and establish the order of details
    # make csv file (append mode so the line we write in isn't deleted)
    f = open("final.csv", "a", newline="")
    # establishes the order of details: order the details will be input, saved, and displayed
    tup1 = ("Title", "Author", "Genre(s)", "Page #", "Rating(_/5)")
    # writes the tuple with the order of details into the csv file
    writer = csv.writer(f)
    writer.writerow(tup1)
    # close the file
    f.close


def book(): # input all the values for your book (ie. title, author, ect) and add to file
    # define all the variables and get user input (all of your book details)
    title = input('Title: ')
    author = input('Author: ')
    genre = input('Genre: ')
    pages = input('Page Count: ')
    rating = input('Rating(_/5): ')
    # open file to add your inputs (append mode so it saves)
    f = open("final.csv", "a", newline="")
    # establishes what order the inputs are supposed to be in
    book_details = (title, author, genre, pages, rating)
    # writes your inputs into the file
    writer = csv.writer(f)
    writer.writerow(book_details)
    # close file
    f.close


def archive(): # open file and read the file
    # get user input: do they want to read the file or not?
    look_at_history = input("Would you like to look at your archive? Input yes if so, input no if otherwise: ")
    # if you answer yes to the question above, code with open csv file in read mode, and print the data for you to read
    while look_at_history == "yes" or look_at_history == "YES" or look_at_history == "Yes":
        with open("final.csv", "r", newline="") as f:
            reader = csv.reader(f)
            # moves to the first line to read
            f.seek(0)
            # read the file and print it to see
            data_read = []
            for row in reader:
                data_read.append(row)
            print(data_read)
        # asks if user would like to add another book after viewing their archive
        more_books()
    # if the user doesn't want to view their archive, ask if they would like to add another book
    else:
        more_books()
        

def more_books(): # add more books to save to the file
    # get user input: do they want to add another book or no?
    add_book = input("Would you like to add a book? Input yes if you wish to add a book: ")
    # if you answer yes to the function above, call the function book() that collects all the input for the new book and adds it to the csv file [look above for more detail]
    if add_book == "yes" or add_book == "YES" or add_book == "Yes":
        book()
        more_books()
    # if the user doesn't want to add another book, asks if they want to see their archive
    else:
        archive()
    
# call the function more_books so all the functions are called and can be executed
more_books()
