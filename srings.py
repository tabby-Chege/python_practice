#strings
#A sequence of characters 
word = "PYTHON"
#creating a string using single quotes
city ='Nairobi'
#creating a string using double quotes
country = "Kenya"
#triple quotes can be used to create a string that spans multiple lines
message = """welcome to python.
Today we are going to learn strings.
Strings are used to store text data in python.
"""
print(message)
#user input ;input() =>input function will always give us a string value.
#username = input("Enter your username: ")
##print(type(username))
#accessing characters in a string
print(message[11]) #accessing the 12th character in the string
#change a character in a string
#srings are immutable in python, we cannot change a character in a astring. we can only create a new sring with the desired changes.
word = "Jython"
print(word)