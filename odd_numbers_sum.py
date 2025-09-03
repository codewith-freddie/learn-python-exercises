
# Task: Write a Python script that calculates the sum of odd numbers between two user-input numbers.
# Use a while loop to iterate from start to end, check if odd, and accumulate the sum.

#LOOPS No. 1

n1 = int(input("Please input a number for starting point: "))
n2 = int(input("Please input a number for ending point: "))
sum = 0

while n1 <= n2:
    if n1 %2 != 0:
        sum += n1
    n1 += 1

print("\nThe sum of odd number is: ", sum)

# Explanation: This script demonstrates the use of while loops combined with if statements for conditional accumulation.
# It iterates from start to end, checks for odd numbers using modulo, and sums them up.
# This example teaches loop control, conditional logic inside loops, and variable accumulation in Python.
# Suggested title: odd_sum_calculator.py
