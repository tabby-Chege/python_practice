#Functions, modules and libraries
#Function is a reusable block of code that performs a specific task
import module_test
import math
import random

inventory={}
def calculate_total(price, quantity):
    total = price * quantity
    return total
first_total = calculate_total(1500, 4)
second_total = calculate_total(2000, 5)
print(first_total)
print(second_total)

#modules are files that contain Python code, which can include functions, classes, and variables. They allow you to organize your code into separate files for better maintainability and reusability. You can import modules into your code using the `import` statement.
module_test.add_product(inventory, "rice", 20, 2000)
module_test.add_product(inventory, "milk", 10, 3000)
module_test.display_inventory(inventory)

#libraries are collection of reusable codes that help us do common tasks. Contains modules, packages, functions, tools, and documentation. Libraries are designed to be used by other programs, making it easier for developers to implement functionality without having to write code from scratch. Python has a rich ecosystem of libraries that cover a wide range of applications, from web development to data analysis and machine learning.
#examples of libraries: maths, datetime, logging.json, random
number = 25
square_root = math.sqrt(number)
print(f"The square root of {number} is: {square_root}") 

random_number = random.randint(1, 10)
print(random_number)
