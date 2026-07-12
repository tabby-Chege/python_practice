class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    def display_details(self):
        print(f"Title:{self.title}")
        print(f"Author:{self.author}")
        print(f"Pages:{self.pages}")

#create instances of book
book1 = Book("python Basics", "Jane", 250)
book2 = Book("The ploygamist", "Sue Nyathi", 500)
book3 = Book("Atomic Habits", "JamesClear", 500)

book1.display_details()
book2.display_details()
book3.display_details()

#__init__ method is a special method in python classes. It is called when an object is created from a class and allows the class to initialize the attributes of the class.