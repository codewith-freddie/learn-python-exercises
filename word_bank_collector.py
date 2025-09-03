# Task: Write a Python script that uses a while loop to collect words from user input into a list.
# Allow the user to continue adding words or stop, then display the collected words.

#Set A : Loop 2

word_bank = []
loop = 1

while True:
    input_word = input("Enter a word to add: ")
    word_bank.append(input_word)

    prompt = input("Try again? ")
    if prompt.lower() == 'yes':
        loop = loop + 1
        continue
    elif prompt.lower() == 'no':
        break
    else:
        print("Invalid input!")

print(f"\nTotal number of words: {loop}")

count = 1
for x in word_bank:
    print(count, x)
    count += 1

# Explanation: This script demonstrates the use of a while loop for user input collection and a for loop for display.
# It includes input validation and list manipulation, teaching loop control, conditionals, and list operations in Python.
# Suggested title: word_bank_collector.py
