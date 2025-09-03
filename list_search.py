
# Task: Write a Python script that searches for a user-input number in a predefined list.
# Print true or false for each element and indicate if a match was found.

list_of_numbers = [9,41,12,3,74,15,3,8,10,3]
isMatch = False

input_num = int(input("Enter the number to search: "))
print(f"Number to search: {input_num}")

print("Before False")
for i in list_of_numbers:
    if i != input_num:
        print(f"False {i}")
        isMatch = False
    elif i == input_num:
        print(f"True {i}")
        isMatch = True
print(f"After {isMatch}")

# Explanation: This script demonstrates searching in a list using a for loop and conditional statements.
# It prints the result for each element and uses a flag to track if a match was found.
# This example teaches loop iteration, conditionals, and flag variables in Python.
# Suggested title: list_search.py


