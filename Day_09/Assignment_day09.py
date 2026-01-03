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
    print("Please Enter a valid niumber :(")