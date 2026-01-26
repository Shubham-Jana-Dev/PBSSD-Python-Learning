# finctions 
# printing my name by using function call
'''
def printing_name():
    print("Shubham Jana")
printing_name()
printing_name()
printing_name()
printing_name()
'''
# another way
"""
def name():
    print("Shubham Jana")
for i in range(100):
    name()
"""
# simple calculator:
'''
def calculator():
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    operator = input("Enter the operator ('+','-','/','%') : ")
    if (operator == '+'):
        print(f"{num1} + {num2} = ",num1+num2)
    elif(operator == '-'):
        print(f"{num1} - {num2} = ", num1-num2)
    elif(operator == '*'):
        print(f"{num1} X {num2} = ", num1*num2)
    elif(operator == '/'):
        if(num2 != 0):
            print(f"{num1} ÷ {num2} = ", num1/num2)
        else:
            print("Please enter a valid a input because no numbeer can not divisible by 0. :(")
    elif(operator == '%'):
        print(f"the remainder of {num1} ÷ {num2} is ", num1%num2)
    else:
        print("Please enter a valid operator.")
calculator()
'''
# another way

first_number = int(input("Enter the first number: "))
second_number = int(input("Enter the second number: "))
operator = input("Enter the operator (one of these '+','-','*','/' and '%'): " )
def addition():
    return first_number + second_number
def subtraction():
    return first_number - second_number
def multiplication():
    return first_number * second_number
def division():
    return first_number / second_number
def remainder():
    return first_number % second_number
if operator == '+':
    print(f" {first_number} + {second_number} =",addition())
elif operator == '-':
    print(f" {first_number} - {second_number} =",subtraction())
elif operator == '*':
    print(f" {first_number} x {second_number} =",multiplication())
elif operator == '%':
    print(f" {first_number} % {second_number} =",remainder())
elif operator == '/':
    if second_number != 0:
        print(f" {first_number} / {second_number} =", division())
    else:
        print("Any number can not divisible by ZERO :(")
else:
    print("Enter a valid operator :(")

    