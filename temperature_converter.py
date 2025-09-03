
# Task: Write a Python script that converts temperature between Fahrenheit and Celsius based on user input.
# The script should handle 'f' for Fahrenheit to Celsius and 'c' for Celsius to Fahrenheit.
# If an invalid unit is entered, display a warning message.
# Finally, print the converted temperature and new unit.

#IF STATEMENT No. 1
temp = float(input("Please enter a temperature: "))
unit = str(input("Please enter a unit: "))
if unit == "f":
    new_temp = (temp - 32) / 1.8
    new_unit = "c"

elif unit == "c":
    new_temp = (temp * 1.8) + 32
    new_unit = "f"

else:
    print("WARNING: Invalid Unit Type !")

print(new_temp, new_unit)

# Explanation: This script demonstrates the use of if-elif-else statements for conditional logic.
# It handles user input for temperature and unit, performs conversion using formulas, and provides a warning for invalid units.
# This example teaches input handling, conditional statements, and basic math operations in Python.
# Suggested title: temperature_converter.py
