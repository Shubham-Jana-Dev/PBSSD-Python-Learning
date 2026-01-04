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
'''
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
'''
# 80. Check whether a given number is a palindrome (logic-based).
'''
num = 121
last_digit = num % 10
first_digit = num // 100
if (first_digit == last_digit):
    print("It's a palindrome number")
else:
    print("It's not a palindrome number")
'''
# 81. Check whether a number is divisible by 3 or 5 but not both.
'''
num = int(input("Enter a number: "))
if (num % 3 == 0 and num % 5 == 0):
    print("Divisible by both ")
elif (num % 3 == 0 or num % 5 == 0):
    print("Divisible by 3 or 5, but not both! (Success) :)")
else:
    print("Not divisible by either. :(")
'''
# 82. Find the day of the week based on number input (1–7).
'''
day = int(input("Enter the number : "))
if (day == 1):
    print("Sunday")
elif(day == 2):
    print("Monday")
elif(day == 3):
    print("Tuesday")
elif(day == 4):
    print("Wednesday")
elif(day == 5):
    print("Thursday")
elif(day == 6):
    print("Friday")
elif(day == 7):
    print("Saturday")
else:
    print("Please enter in between 1 to 7")
'''
#83. Create a traffic light signal system using if-elif.
'''
colour = input("""enter the colour of the Traffic signal 
               R = Red
               Y = Yellow
               G = Green
- """)
if (colour == 'R'):
    print("Stop")
elif(colour == 'Y'):
    print("Look")
elif(colour == 'G'):
    print("Go")
else:
    print("Invalid input :(")
'''
#84. Assign employee level based on experience years.
'''
exp = float(input("""
0 to 2 years	Junior 
2 to 5 years	Intermediate 
5 to 10 years	Senior
Above 10 years	Lead                
Enter the your experience in years: """))
if ( 0 <= exp <2):
    print("Junior")
elif(2 <= exp <5):
    print("Intermediate")
elif(5 <= exp < 10):
    print("Senior")
elif(exp>=10):
    print("Lead")
else:
    print("Invalid input")
'''
#85. Check whether a number is positive, even, and divisible by 5.
'''
s = int(input("Enter the number: "))
if (s>0 and s%2==0 and s%5==0):
    print("the number is positive, even, and divisible by 5.")
else:
    print("number is not positive, even, and divisible by 5.")
'''
#86. Calculate discount based on purchase amount.
'''
print("""
₹500 to ₹1000 --> 10%
upto ₹4000 --> 15%
upto ₹8000 --> 18%         
upto ₹20000 --> 20%
> ₹20000 --> 25%
""")
amount = float(input("Enter the amount : "))
if (500 <= amount <= 1000):
    print("discount = ", amount * 0.1)
elif(1000 < amount <= 4000):
    print("discount = ", amount * 0.15)
elif(4000 < amount <= 8000):
    print("discount = ", amount * 0.18)
elif(8000 < amount <=20000):
    print("discount = ", amount * 0.2)
elif(amount>20000):
    print("discount = ", amount *0.25)
else:
    print("No discount :(")
'''
#87. Determine exam result: Pass, Compartment, or Fail.
'''
result = float(input("""
------------------------------------
<25% --> Fail :(
25% to 30%  --> Compartment
> 30% to 100% --> Pass
-------------------------------------
Enter your result's percentage:  """))
if (0 <= result < 25):
    print("Fail :(")
elif(25 <= result <30):
    print("Compertment :|")
elif(30 <= result <= 100):
    print("Pass :)")
else:
    print("Invalid input")
'''
#88. Check whether a number is divisible by 11 using condition.
'''
r = int(input("Enter the number: "))
if (r%11 == 0):
    print("The number is divisible by 11. :)")
else:
    print("The number is not divisible by 11. :(")
'''
#89. Find the maximum of five numbers using if-elif.
'''
num1 = float(input("num1 = "))
num2 = float(input("num2 = "))
num3 = float(input("num3 = "))
num4 = float(input("num4 = "))
num5 = float(input("num5 = "))
if(num1 > num2 and num1 > num3 and num1 > num4 and num1 > num5):
    print(f"{num1} is maximum (num1)")
elif(num2 > num3 and num2 > num4 and num2 > num5):
    print(f"{num2} is maximum (num2)")
elif(num3 > num4 and num3 > num5):
    print(f"{num3} is maximum (num3)")
elif(num4 > num5):
    print(f"{num4} is maximum (num4)")
else:
    print(f"{num5} is maximum (num5)")
'''
#90. Check whether a given character is a hexadecimal digit.
'''
char = input("Enter a single character: ")
if ("0" <= char <= "9"):
    print("It's a hexadecimal digit.")
elif ("A" <= char <= "F"):
    print("It's a hexadecimal digit.")
elif ("a" <= char <= "f"):
    print("It's a hexadecimal digit.")
else:
    print("It's not a hexadecimal digit.")
'''
#91. Check whether a number lies in multiple ranges.
num = float(input("""
range A: 20 to 40
rnage B: 35 to 100
Enter the number: """))
if (20<=num<=40) and (35<=num<=100):
    print(f"{num} lies between both range A and B.")
else:
    print(f"{num} does not lie between both range A and B.")

# 92. Assign grades using nested if-else.
score = float(input("Enter your score (0-100): "))
if (score >= 0 and score <= 100):

    if (score >= 90):
        print("Grade: A")
    else:
        if (score >= 80):
            print("Grade: B")
        else:
            if (score >= 70):
                print("Grade: C")
            else:
                print("Grade: D/Fail")

else:
    print("Invalid score! Please enter a number between 0 and 100.")