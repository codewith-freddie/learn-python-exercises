

numlist = [9, 50, 62, 65, 139, 154]
ave = 0
val = 0
print("Before", val, val)

count = 0
for i in numlist:
    count += 1
    temp = val
    val = i
    sum = i - temp
    ave = ave + sum
    print(count, i, sum)

print(f"After {count} {i} {ave / count}")