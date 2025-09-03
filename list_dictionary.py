# List and Dictionary Operations in One File

# --- List Operations ---
# 1. Creating a list
my_list = [5, 3, 8, 1, 2]
print("Original List:", my_list)

# 2. Accessing elements
print("First element:", my_list[0])  # Output: 5
print("Last element:", my_list[-1])  # Output: 2

# 3. Modifying elements
my_list[2] = 10
print("Modified List:", my_list)  # Output: [5, 3, 10, 1, 2]

# 4. Appending elements
my_list.append(7)
print("After Append:", my_list)  # Output: [5, 3, 10, 1, 2, 7]

# 5. Inserting elements
my_list.insert(2, 99)  # Insert 99 at index 2
print("After Insert:", my_list)  # Output: [5, 3, 99, 10, 1, 2, 7]

# 6. Removing elements by value
my_list.remove(99)
print("After Remove:", my_list)  # Output: [5, 3, 10, 1, 2, 7]

# 7. Removing elements by index (Pop)
popped_element = my_list.pop(2)
print("Popped Element:", popped_element)  # Output: 10
print("After Pop:", my_list)  # Output: [5, 3, 1, 2, 7]

# 8. Sorting the list
# Sorting the list in ascending order (default)
my_list.sort()
print("Sorted List (Ascending):", my_list)  # Output: [1, 2, 3, 5, 7]

# Sorting in descending order
my_list.sort(reverse=True)
print("Sorted List (Descending):", my_list)  # Output: [7, 5, 3, 2, 1]

# Sorting Discussion:
# .sort() method sorts the list in place, modifying the original list.
# Use reverse=True to sort in descending order.

# 9. Reversing the list
my_list.reverse()  # Reverse the list order
print("Reversed List:", my_list)  # Output: [1, 2, 3, 5, 7]

# 10. Getting the length of the list
print("Length of List:", len(my_list))  # Output: 5

# 11. List slicing
print("Sliced List (index 1 to 4):", my_list[1:4])  # Output: [2, 3, 5]


# --- Dictionary Operations ---
# 1. Creating a dictionary
my_dict = {'name': 'Alice', 'age': 25, 'city': 'New York'}
print("\nOriginal Dictionary:", my_dict)

# 2. Accessing values by key
print("Name:", my_dict['name'])  # Output: Alice

# 3. Modifying values
my_dict['age'] = 26
print("Modified Dictionary:", my_dict)  # Output: {'name': 'Alice', 'age': 26, 'city': 'New York'}

# 4. Adding new key-value pairs
my_dict['email'] = 'alice@example.com'
print("After Adding Email:", my_dict)  # Output: {'name': 'Alice', 'age': 26, 'city': 'New York', 'email': 'alice@example.com'}

# 5. Removing elements by key using pop
removed_age = my_dict.pop('age')
print("Removed Age:", removed_age)  # Output: 26
print("After Removing Age:", my_dict)  # Output: {'name': 'Alice', 'city': 'New York', 'email': 'alice@example.com'}

# 6. Removing the last added item using popitem
last_item = my_dict.popitem()
print("Last Item Removed:", last_item)  # Output: ('email', 'alice@example.com')
print("After popitem:", my_dict)  # Output: {'name': 'Alice', 'city': 'New York'}

# 7. Checking for key existence
print("Is 'name' in dictionary?", 'name' in my_dict)  # Output: True

# 8. Getting all keys, values, and items
print("Keys:", my_dict.keys())   # Output: dict_keys(['name', 'city'])
print("Values:", my_dict.values())  # Output: dict_values(['Alice', 'New York'])
print("Items:", my_dict.items())  # Output: dict_items([('name', 'Alice'), ('city', 'New York')])

# 9. Looping through dictionary items
for key, value in my_dict.items():
    print(f"{key}: {value}")
# Output:
# name: Alice
# city: New York

# 10. Merging two dictionaries
new_dict = {'job': 'Engineer', 'salary': 70000}
my_dict.update(new_dict)
print("After Merging:", my_dict)  # Output: {'name': 'Alice', 'city': 'New York', 'job': 'Engineer', 'salary': 70000}

# 11. Clearing all dictionary items
my_dict.clear()
print("Cleared Dictionary:", my_dict)  # Output: {}


# List of Dictionaries Example
people = [
    {'name': 'Alice', 'age': 25, 'city': 'New York'},
    {'name': 'Bob', 'age': 30, 'city': 'San Francisco'},
    {'name': 'Charlie', 'age': 35, 'city': 'Los Angeles'}
]

# --- Basic Operations on List of Dictionaries ---

# 1. Accessing individual dictionaries
print("First person:", people[0])  # Output: {'name': 'Alice', 'age': 25, 'city': 'New York'}

# 2. Accessing values in a specific dictionary
print("Name of second person:", people[1]['name'])  # Output: Bob

# 3. Modifying a dictionary in the list
people[2]['age'] = 36  # Modify Charlie's age
print("Updated List:", people)

# 4. Adding a new dictionary to the list
new_person = {'name': 'David', 'age': 28, 'city': 'Chicago'}
people.append(new_person)
print("After Adding a New Person:", people)

# 5. Removing a dictionary from the list
removed_person = people.pop(1)  # Remove the dictionary at index 1 (Bob)
print("Removed Person:", removed_person)
print("After Removal:", people)

# 6. Iterating through the list of dictionaries
print("\nIterating through people:")
for person in people:
    print(f"{person['name']} from {person['city']} is {person['age']} years old.")

# 7. Filtering based on a condition
# Get a list of people who are older than 30
older_than_30 = [person for person in people if person['age'] > 30]
print("\nPeople older than 30:", older_than_30)

# 8. Sorting the list of dictionaries by a key (e.g., age)
people.sort(key=lambda person: person['age'])
print("\nSorted by Age:", people)

# Sorting Discussion:
# You can use the 'key' parameter with the sort function to specify which field in the dictionaries should be used for sorting.


#1
fruits = ["apple","banana","avocado","jackfruit"]
print(fruits)

#2
first_fruits = fruits[0]
second_fruits = fruits[1]
print(first_fruits, second_fruits)

#3
new_fruits = fruits[0:3]
print(new_fruits)

#4
fruits[4] = "kiwi"
print(fruits)

#5
fruits.append("pineapple")
fruits.append("mango")

#6
fruits.remove("jackfruit")
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
    print(fruits)

#10
if "apple" in fruits:
    print("yes")

#11
copied_list = fruits.copy()
print(copied_list)
copied_list.append("strawberry")
print(copied_list)

#12
fruits.clear()
print(fruits)