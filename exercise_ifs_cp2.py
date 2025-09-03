
#IF STATEMENT
#CONCEPT IN PRACTICE No. 2

positive_num = int(input("Please enter a positive number:"))
if positive_num < 0:
    print("Negative input set to 0")
    positive_num = 0
print(positive_num)