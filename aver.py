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

for i in range(students):
    name = input(f"\nEnter the name of student {i + 1}: ")
    marks = []
    for j in range(5):
        score = float(input(f"Enter mark {j + 1} for {name}: "))
        marks.append(score)
    grade = calculate_grade(marks)
    print(f"{name} got grade {grade}")
