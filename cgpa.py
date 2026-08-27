import csv
import os

name = input("Enter student full name: ")
subjects = ["Python", "Database", "Maths", "English", "Computer"]
marks = []

print("\n--- Enter Marks (Out of 100) ---")
for subject in subjects:
    while True:
        try:
            mark = float(input(f"Enter marks for {subject}: "))
            if 0 <= mark <= 100:
                marks.append(mark)
                break
            print("Invalid marks! Please enter a value between 0 and 100.")
        except ValueError:
            print("Invalid input! Please enter a numeric value.")

total = sum(marks)
average = total / len(subjects)

# Calculating CGPA based on a standard 10-point scale
cgpa = average / 10

# Grade mapping based on CGPA thresholds
if cgpa >= 9.0:
    grade = "O"
elif cgpa >= 8.0:
    grade = "A+"
elif cgpa >= 7.0:
    grade = "A"
elif cgpa >= 6.0:
    grade = "B+"
elif cgpa >= 5.0:
    grade = "B"
else:
    grade = "F"

result = "PASS" if cgpa >= 5.0 else "FAIL"

# Displaying Results
print(f"\nStudent Name: {name}")
print(f"Total Marks: {total}")
print(f"Average Marks: {average:.2f}")
print(f"Calculated CGPA: {cgpa:.2f}")
print(f"Grade: {grade}")
print(f"Result: {result}")

# Saving data into the CSV file
file_name = "student_cgpa_results.csv"
file_exists = os.path.isfile(file_name)

with open(file_name, mode='a', newline='') as file:
    writer = csv.writer(file)
    if not file_exists:
        writer.writerow(["Name", "Total Marks", "Average Marks", "CGPA", "Grade", "Result"])
    writer.writerow([name, total, f"{average:.2f}", f"{cgpa:.2f}", grade, result])

print(f"\nResult has been saved to '{file_name}' file.")
