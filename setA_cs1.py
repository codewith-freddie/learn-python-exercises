#Set A
#Conditional Statement 1

input_hours = int(input("Enter Hours: "))
hours_rate = float(input("Enter Hours Rate: "))

if input_hours <= 40:
    gross_pay = input_hours * hours_rate
elif input_hours > 40:
    overtime = input_hours - 40
    total = overtime * 1.5 * hours_rate
    gross_pay = total + 40 * hours_rate

print(f"Gross Salary: {gross_pay}")
