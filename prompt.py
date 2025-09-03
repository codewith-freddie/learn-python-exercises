def main():
    while True:
        num1 = int(input("Enter the first integer: "))
        num2 = int(input("Enter the second integer: "))

        operation = input("Select an operation (+, -, *, /): ")

        if operation == '+':
            print(f"The sum of {num1} and {num2} is: {num1 + num2}")
        elif operation == '-':
            print(f"The subtraction of {num2} and {num1} is: {num1 - num2}")
        elif operation == '*':
            print(f"The product of {num1} and {num2} is: {num1 * num2}")
        elif operation == '/':
            if num2 != 0: 
                print(f"The division of {num1} and {num2} is: {num1 / num2}")
            else:
                print("Error: Division by zero is not allowed!")
        else:
            print("Invalid operation. Please select a valid option.")

        
        while True: 
            play_again = input("\nDo you want to date me? (yes/no): ").strip().lower()
            if play_again == 'yes':
                print("See you on friday 6 pm.")
                return
            else:
                print("Invalid response. Please enter 'yes'.")


main()
