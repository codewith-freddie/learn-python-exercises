
#LOOPS
#CONCEPT IN PRACTICE No. 1

f = 1
g = 2
print(f, end='')

while g < 20:
    print(g, end='')
    temp = f
    f = g
    g = temp + g