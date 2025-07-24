# Function to calculate grade based on average
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

# Input: number of students
students = int(input("Enter the number of students: "))

# Open file for writing
with open("student_data.txt", "w") as file:
    file.write("ID\tName\t\tMarks\t\t\t\t\tGrade\n")
    file.write("-" * 60 + "\n")

    # Loop through each student
    for i in range(students):
        student_id = input(f"\nEnter ID for student {i + 1}: ")
        name = input(f"Enter name for student {i + 1}: ")
        marks = []

        for j in range(5):
            score = float(input(f"Enter mark {j + 1} for {name}: "))
            marks.append(score)

        grade = calculate_grade(marks)

        # Write to file
        marks_str = ", ".join([str(m) for m in marks])
        file.write(f"{student_id}\t{name}\t{marks_str}\t{grade}\n")

        # Optional: Print to console
        print(f"{name} (ID: {student_id}) got grade {grade}")

print("\nAll student data has been written to 'student_data.txt'")
