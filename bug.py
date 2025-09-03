while True: 
    play_again = input("\nDo you want to date me? (yes/no): ").strip().lower()
    if play_again == 'yes':
        print("See you on friday 6 pm.")
        break
    else:
        print("Invalid response. Please enter 'yes'.")