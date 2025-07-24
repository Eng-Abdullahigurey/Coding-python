# List & loop:
mark = []

for i in range(5):
    m = float(input("Enter marks: "))
    mark.append(m)

# Print marks to console
print("Marks are:", mark)

# Write to file
with open("marks.txt", "w") as file:
    file.write("Marks are: " + str(mark) + "\n")

print("\nAll marks have been written to 'marks.txt'")
