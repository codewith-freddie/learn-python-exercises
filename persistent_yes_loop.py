# Task: Write a Python script that repeatedly asks the user if they want to date you.
# The script should only accept 'yes' as a valid response.
# If the user inputs 'yes', print a confirmation message and end the program.
# For any other input, prompt the user again until 'yes' is entered.

while True:
    play_again = input("\nDo you want to date me? (yes/no): ").strip().lower()
    if play_again == 'yes':
        print("See you on friday 6 pm.")
        break
    else:
        print("Invalid response. Please enter 'yes'.")

# Explanation: This script demonstrates the use of an infinite loop with a break condition to validate user input.
# It uses input() to get user responses, and string methods strip() and lower() to normalize the input.
# The loop continues until the user enters 'yes', ignoring all other inputs.
# This example teaches input validation, loop control, and basic string handling in Python.
