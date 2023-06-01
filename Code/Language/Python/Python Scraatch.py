#@Python: 
#Code Scratch Work

# Put your code here
print("---")
print("\n?: Calculate salary with overtime. \n")
hrwage = float(input("Enter the hourly wage: ")) #$10
reghours = int(input("Enter the daily hours: ")) #8
overhours = int(input("Enter the overtime hours: ")) #2

daypay = hrwage * reghours
overpay = (hrwage * 1.5 )* overhours 
weekpay = daypay + overpay

#Output
print("The total weekly pay is ",weekpay)
print("---")

#Numbers
#3:21 pm, 
# -------------------------------------------------------------------------------
#Code Scratch Work for 
# Thurs. April 22. 2021
# Year. MM. DD. (day_of_week)
# 2022. 04. 22 (4)

# Put your code here
print("\n?: Calculate if a triangle is equilateral. \n")
side1 = int(input("Enter the first sides length: "))
side2 = int(input("Enter the second sides length: "))
side3 = int(input("Enter the third sides length: "))

if side1 == side2:
    if side2 == side3:
        print("\nThe triangle is equilateral.")
else:
    print("\nThe triangle is not equilateral.")
    print("---")
# ---------------------------------------------------------------------------------------
# Put your code here:

#Input
print("\n?: Calculate if a triangle is a right triangle. \n")
s1 = int(input("Enter the first side: "))
s2 = int(input("Enter the second side: "))
s3 = int(input("Enter the third side: "))

#Process
#s3**2 = (s1**2 + s2**2)
#righttri**2

#Output
#print("\nThe right triangle is:",righttri)
if s3**2 == (s1**2 + s2**2):
    print("\nThe triangle is a right triangle.")
elif s1**2 == (s2**2 + s3**2):
    print("\nThe triangle is a right triangle.")
elif s2**2 == (s1**2 + s3**2):
    print("\nThe triangle is a right triangle.")
else:
    print("\nThe triangle is not a right triangle.")
    print("---")

# ---------------------------------------------------------------------------------------

# Put your code here
print("\n?: Calculate the sum iterations of pi. \n")
n = int(input("Enter the number of iterations: "))
total = 0
for i in range(1,n):
    total += (-1)**(i+1)*((1.0/((i/2)+1)))

value = 4*(1-total)

print("The approximation of pi is ",value)
print("---")


