# Task: Write a Python script that calculates gross pay based on hours worked and hourly rate.
# Include overtime calculation for hours over 40 at 1.5 times the rate.

#Set A
#Conditional Statement 1

input_hours = int(input("Enter Hours: "))
hours_rate = float(input("Enter Hours Rate: "))

if input_hours <= 40:
    gross_pay = input_hours * hours_rate
elif input_hours > 40:
    overtime = input_hours - 40
    total = overtime * 1.5 * hours_rate
    gross_pay = total + 40 * hours_rate

print(f"Gross Salary: {gross_pay}")

# Explanation: This script calculates gross pay with overtime rules using conditional statements.
# It demonstrates input handling, arithmetic operations, and if-elif logic for different pay rates.
# This example teaches basic payroll calculation and conditional branching in Python.
# Suggested title: payroll_calculator.py
