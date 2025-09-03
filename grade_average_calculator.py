
# Task: Write a Python script that takes four subject grades as input, calculates the average, and determines if the student passed or failed.

math = int(input("Math: "))
english = int(input("English: "))
science = int(input("Science: "))
filipino = int(input("Filipino: "))

avg = (math + english + science + filipino) / 4

if avg < 74:
    display = "Failed !"
elif avg >= 75 or avg >= 100:
    display = "Passed !"

print(f"Your average is: {avg}")
print(f"You are {display}")

# Explanation: This script demonstrates input handling, arithmetic operations, conditional statements, and output formatting.
# It calculates the average of four grades and uses if-elif to determine pass/fail status.
# This example teaches user input, calculations, and decision-making in Python.
# Suggested title: grade_average_calculator.py
