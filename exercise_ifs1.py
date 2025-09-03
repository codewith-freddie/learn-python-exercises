
#IF STATEMENT No. 1
temp = float(input("Please enter a temperature: "))
unit = str(input("Please enter a unit: "))
if unit == "f":
    new_temp = (temp - 32) / 1.8
    new_unit = "c"

elif unit == "c":
    new_temp = (temp * 1.8) + 32
    new_unit = "f"

else:
    print("WARNING: Invalid Unit Type !")
    
print(new_temp, new_unit)