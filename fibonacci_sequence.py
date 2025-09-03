
# Task: Write a Python script that demonstrates a simple Fibonacci sequence using a while loop.
# Start with f=1 and g=2, print the sequence values while g is less than 20.

#LOOPS
#CONCEPT IN PRACTICE No. 1

f = 1
g = 2
print(f, end='')

while g < 20:
    print(g, end='')
    temp = f
    f = g
    g = temp + g

# Explanation: This script demonstrates the use of while loops and variable swapping to generate a Fibonacci sequence.
# It prints Fibonacci numbers less than 20, showing loop control and arithmetic operations.
# This example teaches loops, variable assignment, and sequence generation in Python.
# Suggested title: fibonacci_sequence.py
