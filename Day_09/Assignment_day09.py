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