
#LOOPS No. 1

n1 = int(input("Please input a number for starting point: "))
n2 = int(input("Please input a number for ending point: "))
sum = 0

while n1 <= n2:
    if n1 %2 != 0:
        sum += n1
    n1 += 1

print("\nThe sum of odd number is: ", sum)