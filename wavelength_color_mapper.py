
# Task: Write a Python script that determines the color of light based on the input wavelength.
# Use if-elif-else statements to check the wavelength against color ranges (Violet, Blue, Cyan, Green, Yellow, Orange, Red).
# If the wavelength is outside the visible spectrum, display a warning.

#IF STATEMENT No. 3
input_wavelength = int(input("Please enter a light wavelength: "))

if input_wavelength >= 380 and input_wavelength <= 449:
    msg_display = "Violet"

elif input_wavelength >= 450 and input_wavelength <= 484:
    msg_display = "Blue"

elif input_wavelength >= 485 and input_wavelength <= 499:
    msg_display = "Cyan"

elif input_wavelength >= 500 and input_wavelength <= 564:
    msg_display = "Green"

elif input_wavelength >= 565 and input_wavelength <= 589:
    msg_display = "Yellow"

elif input_wavelength >= 590 and input_wavelength <= 624:
    msg_display = "Orange"

elif input_wavelength >= 625 and input_wavelength <= 750:
    msg_display = "Red"

else:
    msg_display = "WARNING: Invalid Input !"

print(msg_display)

# Explanation: This script demonstrates the use of multiple if-elif-else statements for categorizing input into different ranges.
# It assigns colors based on wavelength ranges in the visible spectrum and handles invalid inputs.
# This example teaches conditional logic with ranges, logical operators, and string assignment in Python.
# Suggested title: wavelength_color_converter.py
