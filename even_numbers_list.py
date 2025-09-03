
# Task: Write a Python script that uses a for loop to collect all even numbers from 0 to 100 into a list.

even_num = []

for i in range(101):
    if i %2 == 0:
        even_num.append(i)

print("\nExpected Outcome:")
print(f"Elements of list 'even_num': {even_num}")

# Explanation: This script demonstrates the use of a for loop to iterate through numbers and conditionally append even numbers to a list.
# It shows loop control, modulo operation for even checking, and list manipulation.
# This example teaches iteration, conditionals, and list building in Python.
# Suggested title: even_numbers_list.py
