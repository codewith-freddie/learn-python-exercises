
#LOOPS No. 2

n1 = int(input("Please input a number for starting point: "))
n2 = int(input("Please input a number for ending point: "))

#Displaying odd number
print("\nOdd Numbers:")
num = n1
while num <= n2:
    if num % 2 != 0:
        print(num, end=" ")
    num += 1

#For displaying the descending even numbers
print("\n\nEven Numbers (in descending order):")
num = n2
while num >= n1:
    if num % 2 == 0:
        print(num, end=" ")
    num -= 1
