# Name: Abigail Bui
# Period: 7
# Project Name: My Book Diary
# Time Spent: 

class Book():

    def __init__(self, title, author, genre, pages):
        self.title = title
        self.author = author
        self.genre = genre
        self.pages = pages

    def get_title(self):
        return self.title
    
    def get_author(self):
        return self.author
    
    def get_genre(self):
        return self.genre
    
    def get_pages(self):
        return self.pages

class Read(Book):

    def __init__(self, title, author, genre, pages, rating, notes):
        Book.__init__(self, title, author, genre, pages)
        self.rating = rating
        self.notes = notes
    
    def get_rating(self):
        return self.rating
    
    def get_notes(self):
        return self.notes

class Unread(Book):

    def __init__(self, title, author, genre, pages, why, who):
        Book.__init__(self, title, author, genre, pages)
        self.why = why
        self.who = who
    
    def get_why(self):
        return self.why
    
    def get_who(self):
        return self.who





def original_work():

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

# tkinter testing

import tkinter, tkinter.messagebox
class MyGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.add_unread = tkinter.Button(self.main_window,
            text = 'Add Unread Book',
            command = self.unread_window)
        self.add_read = tkinter.Button(self.main_window,
           text = 'Add Read Book',
           command = self.read_window)
        self.see_booklist = tkinter.Button(self.main_window,
           text = 'See All Books',
           command = self.books_window)
        
        self.add_unread.pack(pady=5)
        self.add_read.pack(pady=5)
        self.see_booklist.pack(pady=5)
        tkinter.mainloop()

    def unread_window(self):
        # this is the title entry
        root = tkinter.Tk()
        root.geometry("300x500")
        title_label = tkinter.Label(root, text = "Title: ")
        title_label.place(x=20, y=10)

        title_entry = tkinter.Entry(root)
        title_entry.place(x=70, y=10)

        # this is the author entry
        author_label = tkinter.Label(root, text = "Author: ")
        author_label.place(x=20, y=40)

        author_entry = tkinter.Entry(root)
        author_entry.place(x=70, y=40)

        # this is the page # entry

        pages_label = tkinter.Label(root, text = "# of Pages: ")
        pages_label.place(x=20, y=70)

        pages_entry = tkinter.Entry(root)
        pages_entry.place(x=100, y=70)

        # this is the 'who recommended' entry

        who_label = tkinter.Label(root, text = "Recommended by: ")
        who_label.place(x=20, y=100)

        who_entry = tkinter.Entry(root)
        who_entry.place(x=140, y=100)

        # this is the checkbutton for genres
        self.top_frame = tkinter.Frame(root)
        self.bot_frame = tkinter.Frame(root)
        
        self.cb_var1 = tkinter.IntVar()
        self.cb_var2 = tkinter.IntVar()
        self.cb_var3 = tkinter.IntVar()
        self.cb_var4 = tkinter.IntVar()
        self.cb_var5 = tkinter.IntVar()
        self.cb_var6 = tkinter.IntVar()
        self.cb_var7 = tkinter.IntVar()
        self.cb_var8 = tkinter.IntVar()
        self.cb_var1.set(0)
        self.cb_var2.set(0)
        self.cb_var3.set(0)
        self.cb_var4.set(0)
        self.cb_var5.set(0)
        self.cb_var6.set(0)
        self.cb_var7.set(0)
        self.cb_var8.set(0)
        
        self.cb1 = tkinter.Checkbutton(self.top_frame,
            text = 'Romance',
            variable = self.cb_var1)
        self.cb2 = tkinter.Checkbutton(self.top_frame,
            text = 'Fantasy',
            variable = self.cb_var2)
        self.cb3 = tkinter.Checkbutton(self.top_frame,
            text = 'Sci-Fi',
            variable = self.cb_var3)
        self.cb4 = tkinter.Checkbutton(self.top_frame,
            text = 'Thriller/Horror',
            variable = self.cb_var4)
        self.cb5 = tkinter.Checkbutton(self.top_frame,
            text = 'Mystery',
            variable = self.cb_var5)
        self.cb6 = tkinter.Checkbutton(self.top_frame,
            text = 'Historical Fiction',
            variable = self.cb_var6)
        self.cb7 = tkinter.Checkbutton(self.top_frame,
            text = 'YA (Young Adult)',
            variable = self.cb_var7)
        self.cb8 = tkinter.Checkbutton(self.top_frame,
            text = 'Nonfiction',
            variable = self.cb_var8)

        
        self.cb1.pack()
        self.cb2.pack()
        self.cb3.pack()
        self.cb4.pack()
        self.cb5.pack()
        self.cb6.pack()
        self.cb7.pack()
        self.cb8.pack()
        self.top_frame.place(x=20, y=130)
        self.bot_frame.place(x=20, y=310)



        # this is the text for  'why to read'

        
        
    def read_window(self):
        tkinter.messagebox.showinfo('Response',
                                    'TBD READ WINDOW')
    def books_window(self):
        tkinter.messagebox.showinfo('Response',
                                    'TBD BOOKS WINDOW')

        
my_gui = MyGUI()

