import tkinter, tkinter.messagebox

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
        root.geometry("300x550")

        self.save = 

        
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

        genre_label = tkinter.Label(root, text = "Genre(s): ")
        genre_label.place(x=20, y=130)
        
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

        # get genre(s)
        genre = []
        if self.cb_var1 == 1:
            genre.append('Romance')
        elif self.cb_var2 == 1:
            genre.append('Fantasy')
        elif self.cb_var3 == 1:
            genre.append('Sci-Fi')
        elif self.cb_var4 == 1:
            genre.append('Thriller/Horror')
        elif self.cb_var5 == 1:
            genre.append('Mystery')
        elif self.cb_var6 == 1:
            genre.append('Historical Fiction')
        elif self.cb_var7 == 1:
            genre.append('YA (Young Adult)')
        elif self.cb_var8 == 1:
            genre.append('Nonfiction')
        
        self.cb1.pack()
        self.cb2.pack()
        self.cb3.pack()
        self.cb4.pack()
        self.cb5.pack()
        self.cb6.pack()
        self.cb7.pack()
        self.cb8.pack()
        self.top_frame.place(x=20, y=160)
        self.bot_frame.place(x=20, y=340)


        # this is the text for  'why to read'
        why_label = tkinter.Label(root, text = "Why to read: ")
        why_label.place(x=20, y=370)
        
        why_text = tkinter.Text(root, height=5, width=30)
        why_text.place(x=20, y=400)



        # this button adds info to file and closes window
        self.quit_button = tkinter.Button(root,
            text = 'Enter',
            command = lambda: self.save=1)
        self.quit_button.place(x=20, y=500)
        if self.save == 1:
            # get title
            title = self.title_entry.get()
            # get author
            author = self.author_entry.get()
            # get pages
            pages = self.pages_entry.get()
            # get who
            who = self.who_entry.get()
            # get why
            why = self.why_text.get()

            # final book info
            book = Unread(title, author, genre, pages, who, why)

            root.destroy


        tkinter.mainloop()
        
    def read_window(self):
        
        root = tkinter.Tk()
        root.geometry("300x550")
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

        # this is the rating entry

        rating_label = tkinter.Label(root, text = "__ out of 10: ")
        rating_label.place(x=20, y=100)

        rating_entry = tkinter.Entry(root)
        rating_entry.place(x=110, y=100)

        # this is the checkbutton for genres

        genre_label = tkinter.Label(root, text = "Genre(s): ")
        genre_label.place(x=20, y=130)
        
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
        self.top_frame.place(x=20, y=160)
        self.bot_frame.place(x=20, y=340)

        # get genre(s)
        genre = []
        if self.cb_var1 == 1:
            genre.append('Romance')
        elif self.cb_var2 == 1:
            genre.append('Fantasy')
        elif self.cb_var3 == 1:
            genre.append('Sci-Fi')
        elif self.cb_var4 == 1:
            genre.append('Thriller/Horror')
        elif self.cb_var5 == 1:
            genre.append('Mystery')
        elif self.cb_var6 == 1:
            genre.append('Historical Fiction')
        elif self.cb_var7 == 1:
            genre.append('YA (Young Adult)')
        elif self.cb_var8 == 1:
            genre.append('Nonfiction')


        # this is the text for final thoughts
        notes_label = tkinter.Label(root, text = "Final thoughts: ")
        notes_label.place(x=20, y=370)
        
        notes_area = tkinter.Text(root, height=5, width=30)
        notes_area.place(x=20, y=400)

        # this button adds info to file and closes window
        self.quit_button = tkinter.Button(root,
            text = 'Enter',
            command = root.destroy)
        self.quit_button.place(x=20, y=500)

        tkinter.mainloop()

        # get title
        title = self.title_entry.get()
        # get author
        author = self.author_entry.get()
        # get pages
        pages = self.pages_entry.get()
        # get who
        who = self.who_entry.get()
        # get why
        why = self.why_text.get()

    def books_window(self):
        root = tkinter.Tk()
        

        
my_gui = MyGUI()
