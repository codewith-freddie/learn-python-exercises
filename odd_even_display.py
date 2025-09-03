
# Task: Write a Python script that displays odd numbers in ascending order and even numbers in descending order between two user-input numbers.
# Use while loops to iterate and print the numbers based on their parity.

#LOOPS No. 2

n1 = int(input("Please input a number for starting point: "))
n2 = int(input("Please input a number for ending point: "))

#Displaying odd number
print("\nOdd Numbers:")
num = n1
while num <= n2:
    if num % 2 != 0:
        print(num, end=" ")
    num += 1

#For displaying the descending even numbers
print("\n\nEven Numbers (in descending order):")
num = n2
while num >= n1:
    if num % 2 == 0:
        print(num, end=" ")
    num -= 1

# Explanation: This script demonstrates the use of while loops for displaying numbers in different orders based on conditions.
# It uses two loops: one for ascending odd numbers and one for descending even numbers.
# This example teaches loop control, conditional logic, and printing with custom separators in Python.
# Suggested title: number_display_loops.py
