
# Task: Write a Python script that checks if the entered car speed is within the good driving range (45-70 km/h).
# If the speed is within the range, print "Good driving".
# Otherwise, print "Follow the speed limits".

#IF STATEMENT No. 2
car_speed = int(input("Please enter a car speed: "))

if car_speed >= 45 and car_speed <= 70:
    print("Good driving")
else:
    print("Follow the speed limits")

# Explanation: This script demonstrates the use of if-else statements with logical operators (and).
# It checks if the input speed is within a specified range and provides appropriate feedback.
# This example teaches conditional logic, logical operators, and input validation in Python.
# Suggested title: speed_checker.py
