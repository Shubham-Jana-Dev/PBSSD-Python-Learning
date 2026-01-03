# Create a menu-driven program for arithmetic operations using if-elif.
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
#Calculate income tax based on salary slabs using if-elif.
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