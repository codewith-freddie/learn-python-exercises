
# Task: Write a Python script that demonstrates sequential if statements modifying a variable.
# Start with num = -10, check if negative and set to 25, then check if less than 100 and add 50, then print the result.

#IF STATEMENT
#CONCEPT IN PRACTICE No. 1

num = -10

if num < 0:
    num = 25
if num < 100:
    num = num + 50
print(num)

# Explanation: This script demonstrates the use of sequential if statements to modify a variable step by step.
# It shows how conditions are evaluated independently, allowing multiple changes to the same variable.
# This example teaches basic conditional logic, variable assignment, and the difference between if and elif in Python.
# Suggested title: sequential_if_demo.py
