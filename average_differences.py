

# Task: Write a Python script that uses a for loop to calculate the average of differences between consecutive elements in a list.

numlist = [9, 50, 62, 65, 139, 154]
ave = 0
val = 0
print("Before", val, val)

count = 0
for i in numlist:
    count += 1
    temp = val
    val = i
    sum = i - temp
    ave = ave + sum
    print(count, i, sum)

print(f"After {count} {i} {ave / count}")

# Explanation: This script demonstrates the use of a for loop to calculate differences between consecutive list elements and their average.
# It uses temporary variables to track previous values and accumulates the sum of differences.
# This example teaches loop iteration, variable management, and basic arithmetic in Python.
# Suggested title: average_differences.py
