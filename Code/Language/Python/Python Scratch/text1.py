print("---")
print("\n?: Calculate the salary (per year) with annual increases over a number of years. \n")

salary = float(input("Enter the starting salary: $"))
percent = float(input("Enter the annual % increase: "))
years = int(input("Enter the number of years: "))
print()
print("Year   Salary")
print("-------------")
for i in range(1,years+1):
    print(i,"  ",end="")
    print("%.2f"%salary)
    salary = salary * (1+percent/100)
