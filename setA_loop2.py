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
