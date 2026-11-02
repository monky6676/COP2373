import csv

with open('grades.csv', 'r', newline='') as csvfile:
    reader = csv.reader(csvfile)

    print("-" * 75)
    print(f"{'First Name':<15} {'Last Name':<15} {'Exam 1':<15} {'Exam 2':<15} {'Exam 3':<15}")
    print("-" * 75)

    next(reader)

    for row in reader:
        print(f"{row[0]:<15} {row[1]:<15} {row[2]:<15} {row[3]:<15} {row[4]:<15}")

    print("-" * 75)