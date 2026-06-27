#LOOPS
#TYPYES OF LOOPS 
#1.FOR LOOPS => used to iterate over a sequence (list, tuple, string) or other iterable objects
#S2.WHILE LOOPS => used to execute a block of code as long as a specified condition is true

#For loop
#for item in sequence:
    # block of sequence is a list, tuple, string or other iterable object

#for number in range(10): #range(start, stop, step)
    #print(number) #0 1 2 3 4 5 6 7 8 9

#for number in range(1, 6): #iterating over a list
    #print(number) #1 2 3 4 5

#for number in range(2, 11, 2): #iterating with a step
    #print(number)

students = ["John", "Alice", "Steven", "Jesca", "Grace", "Kevin"]
for student in students:
    print(student) #John Alice Steven Jesca Grace Kevin

    scores = [80, 45, 90, 30, 60]
for score in scores:
    if score >= 50:
        print("passed") #passed passed passed
    else:
        print(f"{score}, failed") #failed failed
        print ("score, failed") #failed failed

    #While loop it going to be running as long as the condition is true
    #while condition:
        #code to execute
count = 1
while count <= 10:
    print (count)
    count += 1 #count = count + 1
