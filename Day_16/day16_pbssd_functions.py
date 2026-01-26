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