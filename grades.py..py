# Prompt the user to enter their mark
mark = int(input("Enter the student's mark: "))

# Determine the grade based on the mark
if 70 <= mark <= 100:
    grade = "A"
elif 60 <= mark <= 69:
    grade = "B"
elif 50 <= mark <= 59:
    grade = "C"
elif 40 <= mark <= 49:
    grade = "D"
elif 30 <= mark <= 39:
    grade = "E"
elif 20 <= mark <= 29:
    grade = "F"
else:
    grade = "Invalid mark. Please enter a value between 20 and 100."

# Print the result
print(f"The grade is: {grade}")
