#logical operators (and, or, not)
#end operators => all conditions must be true
score = 40
attendance = 95
print(score >= 50 and attendance >= 90) #True

#or operators => at least one condition must be true

score = 30
attendance = 100
print(score >=60 or attendance >=85) 

#not operator => reverses the result of the condition
is_student_active = True
print(not is_student_active) #False

#conditional statements (if, elif, else)
#if statement => executes a block of code if the condition is true
#if condition:
    #code_to_run
    #important rule: Indetation is important in python, it is used to define a block of code
    #elif statement => checks another condition if the previous condition is false
    #if statement is false, it will check the elif condition
    #else statement => executes a block of code if all previous conditions are false

age =16
if age >= 18: 
    print("this person is an adult") #this person is an adult
else:
    print("this person is a minor") #this person is a minor

#elif
#if condition 1:
    #code_to_run_if_condition1 is true
    
#elif condition2:
    #code_to_run_if_condition2 is true
    
#else:
    #run if all conditions are false
    

