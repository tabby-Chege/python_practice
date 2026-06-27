#print("student Progress Checker")
#print("..........")
student_name = input("Enter student name: ")
lab_score = float(input("Enter lab score: "))
Project_score = float(input("Enter project score: "))
Attendance = float(input("Enter attendance percentage: "))
completed_labs = int(input("Enter number of completed labs: "))
active_input = input("Is the student active? (yes/no): ")
if active_input.lower() == "yes":
    avarage_score = (lab_score + Project_score) / 2
if avarage_score >= 50 and Attendance >= 90 and completed_labs >= 8 and active_input.lower() == "yes":
    print(student_name, "Pass.")
else:
    print(student_name, "Fail.")

    