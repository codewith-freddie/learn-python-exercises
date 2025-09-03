
# Task: Write a Python script that allows the user to select a meal from lunch or dinner options.
# First, ask for lunch or dinner, display the corresponding menu.
# Then, ask for the meal choice number and display the selected meal using nested if statements.

#IF STATEMENT No. 4
menu_choice = str(input("Please enter if lunch or dinner : "))

if menu_choice == "lunch":
    display_msg = "1. Ceasar salad \n2. Spicy chicken wrap \n3. Butternut squash soup"

elif menu_choice == "dinner":
    display_msg = "1. Baked salmon \n2. Turkey Burger \n3. Mushroom risotto"

print("\nLunch Meal Option\n\n" + display_msg + "\n")

#FOR SELECTING MEAL OPTION
meal_choice = str(input("Please enter your meal choice number : "))

if menu_choice == "lunch" and meal_choice == "1":
    selected_meal = "Ceasar salad"
elif menu_choice == "lunch" and meal_choice == "2":
    selected_meal = "Spicy chicken wrap"
elif menu_choice == "lunch" and meal_choice == "3":
    selected_meal = "Butternut squash soup"

elif menu_choice == "dinner" and meal_choice == "1":
    selected_meal = "Baked salmon"
elif menu_choice == "dinner" and meal_choice == "2":
    selected_meal = "Turkey Burger"
elif menu_choice == "dinner" and meal_choice == "3":
    selected_meal = "Mushroom risotto"

else:
    print("WARNING: Invalid Input !")


print("\nYou order: " + selected_meal)


# Explanation: This script demonstrates the use of if-elif-else statements for menu selection and nested conditions.
# It handles user input for meal type and choice, assigns the selected meal, and provides a warning for invalid inputs.
# This example teaches conditional logic, logical operators (and), and string handling in Python.
# Suggested title: meal_selector.py

     

