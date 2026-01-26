# finctions 
# There is mainly 2 types of functions
# 1. Built in function (print(),rnage(),sum(),len(),etc)  
# 2. User defined function (crated by users for some spcific requirments)
# rules of naming a function is similer to the rules of naming a variable
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
"""
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
"""
'''
def happy_birth_day(name,age):
    print(f"Happy Birth day {name}")
    print(f"Now you are {age} years old.")
happy_birth_day("Shubham",19)
happy_birth_day("Rahul",21)
'''
# returning string
"""
def My_name(first_name,last_name):
    first_name =first_name.capitalize()
    last_name = last_name.capitalize()
    return first_name + " " + last_name
full_name = My_name("Shubham","Jana")
print(full_name)
bros_name = My_name("Rahul","Roy")
print(bros_name)
Course_name = My_name("B.tech","in CSE")
print(Course_name)
def calculate_school_fees(amount,time):   # the pass keyword do nothing inside a function we use it just because to use the function later.
    pass
School_name = My_name("La","Martinieres for boys")
print(School_name)
"""
# Anonymous function (or Lambda functions)
# This function has not names... that's why we call is anonymous function 
# A lambda function can have multiple parameters....
# A lambda function must be written in a single line of code....
# The syntax of lambda function is diffrent from a ragular functions....
# A lambda function does not need a return statment....
'''
syntax : 
variable_name = lanmbda parametes: expression
'''
dubb = lambda x: x*2
print(dubb(3)) # using a single paramerter

addition = lambda x,y: x+y
print(addition(4,3)) # using multiple parameters

max_value = lambda t,z: t if t>z else z # we can also write conditional statements using lambda functions
print(max_value(5,8))

full_name = lambda first,last: first + " " + last # we can use lambda function to concatinate 2 strings
print(full_name("Shubham","Jana"))

is_even = lambda x : "Even" if x%2 == 0 else "Odd"
print(is_even(8))
# or we can write
is_odd = lambda x: x%2 !=0
print(is_odd(6))
"""
def square (num) :
    return num ** 2
def cube (num) :
    return num ** 3
def transform_list(num_list,transform_items):
    transformed_01 = transform_items(num_list[0])
    transformed_02 = transform_items(num_list[1])
    return[transformed_01,transformed_02]
my_list = [2, 3]
e = transform_list (my_list, square)
print(e)
"""