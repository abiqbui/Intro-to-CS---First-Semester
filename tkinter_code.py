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
    def __str__(self):
        return f"{self.title}, {self.author}, {self.genre}, {self.pages}, {self.rating}, {self.notes}"

class Unread(Book):

    def __init__(self, title, author, genre, pages, why, who):
        Book.__init__(self, title, author, genre, pages)
        self.why = why
        self.who = who
    
    def get_why(self):
        return self.why
    
    def get_who(self):
        return self.who
    def __str__(self):
        return f'{self.title}, {self.author}, {self.genre}, {self.pages}, {self.why}, {self.who}'


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

        self.unread_books = set()
        self.read_books = set()
        tkinter.mainloop()

    def unread_window(self):
    
        root = tkinter.Tk()
        root.geometry("300x550")

        # this is the title entry
        self.title_label = tkinter.Label(root, text = "Title: ")
        self.title_label.place(x=20, y=10)

        self.title_entry = tkinter.Entry(root)
        self.title_entry.place(x=70, y=10)

        

        # this is the author entry
        self.author_label = tkinter.Label(root, text = "Author: ")
        self.author_label.place(x=20, y=40)

        self.author_entry = tkinter.Entry(root)
        self.author_entry.place(x=70, y=40)

        

        # this is the page # entry

        self.pages_label = tkinter.Label(root, text = "# of Pages: ")
        self.pages_label.place(x=20, y=70)

        self.pages_entry = tkinter.Entry(root)
        self.pages_entry.place(x=100, y=70)

        

        # this is the 'who recommended' entry

        self.who_label = tkinter.Label(root, text = "Recommended by: ")
        self.who_label.place(x=20, y=100)

        self.who_entry = tkinter.Entry(root)
        self.who_entry.place(x=140, y=100)

        

        # this is the checkbutton for genres

        self.genre_label = tkinter.Label(root, text = "Genre(s): ")
        self.genre_label.place(x=20, y=130)
        
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


        # this is the text for  'why to read'
        self.why_label = tkinter.Label(root, text = "Why to read: ")
        self.why_label.place(x=20, y=370)
        
        self.why_text = tkinter.Text(root, height=5, width=30)
        self.why_text.place(x=20, y=400)


        # these buttons adds info to file and closes window
        self.enter_button = tkinter.Button(root,
            text = 'Enter',
            command = self.get_unread_info)
        self.enter_button.place(x=20, y=500)

        self.quit_button = tkinter.Button(root,
            text = 'Quit',
            command = root.destroy)
        self.quit_button.place(x=65, y=500)

        tkinter.mainloop()
        
    def get_unread_info(self):
        # get title
        title = str(self.title_entry.get())
        # get author
        author = str(self.author_entry.get())
        # get pages
        pages = str(self.pages_entry.get())
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
        # get who
        who = str(self.who_entry.get())
        # get why
        why = str(self.why_text.get(1.0))
        # final book info
        book = Read(title, author, genre, pages, who, why)
        self.unread_books.add(book.__str__())
        tkinter.messagebox.showinfo("Entered", f"You added {title} by {author}!")

            
        
    def read_window(self):
    
        root = tkinter.Tk()
        root.geometry("300x550")

        # this is the title entry
        self.title_label = tkinter.Label(root, text = "Title: ")
        self.title_label.place(x=20, y=10)

        self.title_entry = tkinter.Entry(root)
        self.title_entry.place(x=70, y=10)

        

        # this is the author entry
        self.author_label = tkinter.Label(root, text = "Author: ")
        self.author_label.place(x=20, y=40)

        self.author_entry = tkinter.Entry(root)
        self.author_entry.place(x=70, y=40)

        

        # this is the page # entry

        self.pages_label = tkinter.Label(root, text = "# of Pages: ")
        self.pages_label.place(x=20, y=70)

        self.pages_entry = tkinter.Entry(root)
        self.pages_entry.place(x=100, y=70)

        

        # this is the rating entry

        self.rating_label = tkinter.Label(root, text = "__ out of 10: ")
        self.rating_label.place(x=20, y=100)

        self.rating_entry = tkinter.Entry(root)
        self.rating_entry.place(x=140, y=100)

        

        # this is the checkbutton for genres

        self.genre_label = tkinter.Label(root, text = "Genre(s): ")
        self.genre_label.place(x=20, y=130)
        
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


        # this is the text for  final thoughts
        self.notes_label = tkinter.Label(root, text = "Final thoughts: ")
        self.notes_label.place(x=20, y=370)
        
        self.notes_text = tkinter.Text(root, height=5, width=30)
        self.notes_text.place(x=20, y=400)


        # these buttons adds info to file and closes window
        self.enter_button = tkinter.Button(root,
            text = 'Enter',
            command = self.get_read_info)
        self.enter_button.place(x=20, y=500)

        self.quit_button = tkinter.Button(root,
            text = 'Quit',
            command = root.destroy)
        self.quit_button.place(x=65, y=500)

        tkinter.mainloop()
        
    def get_read_info(self):
        # get title
        title = str(self.title_entry.get())
        # get author
        author = str(self.author_entry.get())
        # get pages
        pages = str(self.pages_entry.get())
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
        # get rating
        rating = str(self.rating_entry.get())
        # get notes
        notes = str(self.notes_text.get(1.0))
        # final book info
        book = Unread(title, author, genre, pages, rating, notes)
        self.read_books.add(book.__str__())
        tkinter.messagebox.showinfo("Entered", f"You added {title} by {author}!")

            

    def books_window(self):
        root = tkinter.Tk()

        all_books = self.unread_books.union(self.read_books)

        print(all_books)

        self.listbox = tkinter.Listbox(root,
                                       height = 7,
                                       width = 12)


        for book in all_books:
            self.listbox.insert(tkinter.END,book)

        self.quit_button = tkinter.Button(root,
            text = 'Quit',
            command = root.destroy)

        self.listbox.pack()
            
        self.quit_button.pack(side = 'bottom')
        
        tkinter.mainloop()
            




        
        
        

        
my_gui = MyGUI()
