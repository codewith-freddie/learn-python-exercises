
math = int(input("Math: "))
english = int(input("English: "))
science = int(input("Science: "))
filipino = int(input("Filipino: "))

avg = (math + english + science + filipino) / 4

if avg < 74:
    display = "Failed !"
elif avg >= 75 or avg >= 100:
    display = "Passed !"

print(f"Your average is: {avg}")
print(f"You are {display}")