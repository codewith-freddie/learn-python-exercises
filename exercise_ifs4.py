
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

     

