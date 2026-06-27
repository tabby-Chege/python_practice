# Collection Data Types in Python (list, set, tuple, dictionary)

# List: a collection used to store multiple value in one variable. They must be ordered, changeable and allow duplicate values. Lists are defined using square brackets []
books = ["Python Basics", "JavaScript guide", "HTML & CSS", "Flask Fundamentals"]
print(books)
#update the list by adding a new book
books[1] = "Advanced JavaScript"
print(books)
#add items in a list using append()
#  method1: add an item to the end of the list
books.append("Introduction to Git and Github")
print(books)
#method2: add an item at a specific index using insert() method
books.insert(1, "Data Science with Python")
print(books)
#remove an item from a list  
# method1: remove() an item by value
books.remove("HTML & CSS")
print(books)
#method2: pop() an item by index
books.pop(4)
print(books)

books.pop()
print(books)
#checking list length using len() function
#len()
print(len(books))
#loop through a list using for loop
for book in books:
    print(book) #
#list with mixed data types
book_info = ["Python Basics", 5000, 4.5, True]
students_scores =[4, 67, 100, 89, 67, 56, 90,89]
print(students_scores)

# Tuple: a collection used to store multiple value in one variable. They must be ordered and unchangeable. Tuples are defined using parentheses ()
#tuples: ordered, not changeable, allows duplicate values
library_sections = ("Fiction", "Science","Technology", "History")
print(library_sections)
print(library_sections[2]) #Technology
print(library_sections[-1]) #History
print(library_sections[1:3]) #('Science', 'Technology')
print(len(library_sections)) #4
#tuples are not changeable, but you can convert a tuple to a list and then change it
library_list = list(library_sections)
library_list[2] = "Poetry"
library_sections = tuple(library_list)
print(library_sections)
#tuple methods:
#method1: count() => returns the number of times a specified value occurs in a tuple
student_names = ("Edwin", "Tabby", "Yasir", "Prince", "Tabby", "Ziza", "Tereziah", "Okech", "Okech")
print(student_names.count("Yasir"))
#method2: index() 
print(student_names.index("Okech"))




# Set: stores unique values. They are ordered
Courses = {"Introduction to programing", "CyberSecurity Basics", "C++ Programing", "Mobile Development"}
print(Courses)
#add item to a set
#add() 1 item to a set
Courses.add("DataScience")
print(Courses)
#update multiple items to a set
Courses.update(["AI", "Machine Learning"])
print(Courses)
#remove()
Courses.remove("Introduction to programing")
print(Courses)
#discard
Courses.discard("Python Basics")
print(Courses)
#set operation
#union
online_coures = {"Introduction to Programing","CyberSecurity Basics", "C++ Programing", "AI", "UI Design"}
offline_courses={"Mobile Development", "AI", "UI Design"}
all_courses = online_coures.intersection(offline_courses)
print(all_courses)


# Dictionary: store data in key value pairs

