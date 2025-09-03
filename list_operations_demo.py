# Task: Write a Python script demonstrating various list operations in Python.
# Operations include indexing, slicing, modifying, appending, removing, sorting, length checking, iteration, membership testing, copying, and clearing.

#1
fruits = ["apple","banana","orange","avocado","jackfruit"]
print(fruits)

#2
first_fruits = fruits[0]
last_fruits = fruits[-1]
print(first_fruits)
print(last_fruits)

#3
new_fruits = fruits[0:3]
print(new_fruits)

#4
fruits[1] = "kiwi"
print(fruits)

#5
fruits.append("pineapple")
fruits.append("mango")
print(fruits)

#6
fruits.remove("orange")
print(fruits)

#7
fruits.sort()
print(fruits)

fruits.sort(reverse=True)
print(fruits)

#8
print(len(fruits))

#9
for i in fruits:
    print(i)

#10
if "apple" in fruits:
    print("yes")
elif "apple" in fruits:
    print("no")

#11
copied_list = fruits.copy()
print(copied_list)
copied_list.append("strawberry")
copied_list[3] = "water melon"
print(fruits)
print(copied_list)

#12
fruits.clear()
print(fruits)

# Explanation: This script demonstrates a wide range of list operations in Python.
# It covers accessing elements, slicing, modifying, adding, removing, sorting, checking length, iterating, membership testing, copying, and clearing lists.
# This example teaches fundamental list manipulation techniques essential for Python programming.
# Suggested title: list_operations_demo.py
