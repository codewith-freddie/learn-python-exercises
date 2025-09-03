
# Task: Write a Python script that validates user input for a positive number.
# If the input is negative, set it to 0 and display a message, then print the final value.

#IF STATEMENT
#CONCEPT IN PRACTICE No. 2

positive_num = int(input("Please enter a positive number:"))
if positive_num < 0:
    print("Negative input set to 0")
    positive_num = 0
print(positive_num)

# Explanation: This script demonstrates input validation using if statements.
# It checks if the user input is negative, sets it to 0 if so, and provides feedback.
# This example teaches input handling, conditional logic, and default value assignment in Python.
# Suggested title: positive_input_validator.py
