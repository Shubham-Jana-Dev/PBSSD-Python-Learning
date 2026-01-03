# 71. Create a menu-driven program for arithmetic operations using if-elif.
'''
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
opereter = input("Enter the opereter (with in '+','-','*','/'): ")
if (opereter == '+'):
    print(f"The addition of {num1} and {num2} is ", (num1+num2))
elif (opereter == '-'):
    print(f"The substraction of {num1} and {num2} is ",(num1-num2))
elif(opereter == '*'):
    print(f"The Multiplication of {num1} and {num2} is ",(num1*num2))
elif(opereter == '/'):
    if(num2 != 0):
        print(f"The Division of {num1} and {num2} is ", (num1/num2))
    else:
        print(f"any number cannot be divisible by zero.")
else:
    print("You have chosen a invalid input as the oparetor. :(")
'''
# 72. Calculate income tax based on salary slabs using if-elif.
'''
print("""
income >= 10000 = 0%
10000 < income <= 50000 = 15%
50000 < income <= 80000 = 20%
80000 < income <= 100000 = 25%
100000 < income = 30%
      """)
income = float(input("Enter your tax : "))
tax = 0
if (income <= 10000):
    print("No tax :)")
elif ( income <= 50000):
    tax = (income - 10000)* 0.15
    print(f"HI Unfortunately you have to pay ₹ {tax} as tax :)")
elif (income <= 80000):
    tax = (40000 * 0.15) + (income - 50000) * 0.2
    print(f"HI Unfortunately you have to pay ₹ {tax} as tax :)")
elif (income <= 100000):
    tax = (40000 * 0.15) + (30000 * 0.2) + (income - 80000)*0.25
    print(f"HI Unfortunately you have to pay ₹ {tax} as tax :)")
else:
    tax = (40000 * 0.15) + (30000 * 0.2) + (20000*0.25) + (income - 100000)*0.3
    print(f"HI Unfortunately you have to pay ₹ {tax} as tax :)")
'''
# 73. Determine grade based on percentage with multiple conditions.
'''
print("""
marks >= 0 = f
10 < marks <= 50 = D
50 < marks <= 60 = C
60 < marks <= 80 = B
80 < marks <= 90 = A
90 < marks <= 100 = A+
      """)
marks = float(input("Enter your marks's percentage: "))
if (marks <= 10 and marks >=0 ):
    print("F")
elif (10 < marks <= 50):
    print("D")
elif(50 < marks <= 60):
    print("C")
elif(60 < marks <= 80):
    print("B")
elif(80 < marks <= 90):
    print("A")
elif(90 < marks <= 100):
    print("A+")
else:
    print("Please Enter a valid number :(")
'''
# 74. Create a simple calculator using if-elif-else.
'''
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
opereter = input("Enter the opereter (with in '+','-','*','/'): ")
if (opereter == '+'):
    print(f" {num1} + {num2} = ", (num1+num2))
elif (opereter == '-'):
    print(f" {num1} - {num2} = ",(num1-num2))
elif(opereter == '*'):
    print(f" {num1} * {num2} = ",(num1*num2))
elif(opereter == '/'):
    if(num2 != 0):
        print(f" {num1} / {num2} = ", (num1/num2))
    else:
        print(f"any number cannot be divisible by zero.")
else:
    print("You have chosen a invalid input as the oparetor. :(")
'''
# 75. Check whether a triangle is right-angled, acute, or obtuse.
'''
a = float(input("Enter the value of first angle: "))
b = float(input("Enter the value of second angle: "))
c = float(input("Enter the value of third angle: "))
if ((a+b+c == 180) and a > 0 and b > 0 and c > 0):
    if(a == 90 or b == 90 or c == 90):
        print("It's a Right-Angled Triangle.")
    elif(a > 90 or b > 90 or c > 90):
        print("It's a Obtuse-Angled Triangle.")
    elif(a < 90 and b < 90 and c <90):
        print("It's a Acute-Angled Triangle.")
else:
    print("The value of the angles could not create a triangle. :(")
'''
#76. Check whether three sides can form a valid triangle
'''
a = float(input ("Enter the first value of side: "))
b = float(input ("Enter the second value of side: "))
c = float(input ("Enter the third value of side: "))
if(a+b>c and b+c>a and c+a>b):
    print("They can form a triangle. :)")
else:
    print("They can not create a triangle. :(")
'''
#77. Determine eligibility for exam based on attendance percentage.
'''
att = float(input("Enter the percentage of your attendance: "))
if (att>=75 and att<=100):
    print("You are eligible for the exam. :)")
elif(0<=att<75):
    print("You are not eligible for the exam. :(")
else:
    print("Please enter a valid input :(")
'''
#78. Find the quadrant of a point (x, y).
'''
x = float(input("Enter the value of x: "))
y = float(input ("Enter the value of y: "))
if (x == 0 and y != 0 ):
    print(" It's on the Y axis")
elif(y == 0 and x != 0 ):
    print(" It's on the X axis")
elif(x > 0 and y > 0):
    print(" It's in the first quadrant.")
elif(x > 0 and y < 0 ):
    print(" It's in the fourth quadrant.")
elif(x < 0 and y > 0):
    print(" It's in the second quadrant.")
elif(x < 0 and y < 0):
    print(" It's in the third quadrant.")
else:
    print(" It's in the (0,0) point.")
'''
# 79. Determine the type of roots of a quadratic equation.
a = float(input("Enter a = "))
b = float(input("Enter b = "))
c = float(input("Enter c = "))
d = b**2 - (4*(a*c))
if (d==0):
    print("Real and Equal")
elif ( d > 0):
    print("Real and Distinct")
else:
    print("Complex or Imaginary")

