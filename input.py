# Students grade calculation system

def calculate_grade(marks):
    average = sum(marks) / len(marks)
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"

students = int(input("Enter the number of students: "))

with open("student_grades.txt", "w") as file:
    for i in range(students):
        name = input(f"\nEnter the name of student {i + 1}: ")
        marks = []
        for j in range(5):
            score = float(input(f"Enter mark {j + 1} for {name}: "))
            marks.append(score)
        grade = calculate_grade(marks)
        # Write to file
        file.write(f"Student: {name}\n")
        file.write(f"Marks: {marks}\n")
        file.write(f"Grade: {grade}\n\n")
        # Optional: Also print to console
        print(f"{name} got grade {grade}")

print("\nAll student grades have been written to 'student_grades.txt'")
