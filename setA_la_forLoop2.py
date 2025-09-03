
list_of_numbers = [9,41,12,3,74,15,3,8,10,3]
isMatch = False

input_num = int(input("Enter the number to search: "))
print(f"Number to search: {input_num}")

print("Before False")
for i in list_of_numbers:
    if i != input_num:
        print(f"False {i}")
        isMatch = False
    elif i == input_num:
        print(f"True {i}")
        isMatch = True
print(f"After {isMatch}")


