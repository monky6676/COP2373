import csv

with open("grades.csv", "a", newline="") as file:
    writer = csv.writer(file)
#Opens CSV File

    if file.tell() == 0:
        writer.writerow(["First Name", "Last Name", "Exam Grade 1", "Exam Grade 2", 'Exam Grade 3'])

    num_students = int(input("Enter Number of Students Who Were Tested: "))

#Gets Amount of students to be entered

    for i in range(num_students):
        print("\nEnter Student Information", i + 1)
        first_name = input("Enter First Name: ")
        last_name = input("Enter Last Name: ")
        exam1 = input("Enter Exam Grade 1: ")
        exam2 = input("Enter Exam Grade 2: ")
        exam3 = input("Enter Exam Grade 3: ")

#Gets the students information

        writer.writerow([first_name, last_name, exam1, exam2, exam3])

#Writes all the students info in the filee

    print("\nStudents Grades have beeen saved to grades.csv.")

