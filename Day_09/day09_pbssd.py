# Check a digit vs character recognition
'''
e = input("Enter a char....")
if('0'<=e<='9'):
    print("It's a digit")
else:
    print("It's a charecter")
'''
# positive/negative even/odd analysis
'''
x = int(input("Enter number:-"))
if(x>=0):
    if(x%2 == 0):
        print("Positive and even")
    else:
        print("Positive and odd")
else:
    if(x%2 == 0):
        print("Nagetive and even")
    else:
        print("Nagetive and odd")
'''
# character classification
'''
char = input("Enter alfabet:-")
if char >= 'A' and char <= 'Z':
    print("Uper case")
else:
    print("Lower case")
'''
#
'''
char = input("Enter it ....")
if('0'<=char<='9'):
    print("It's a number")
else:
    print("It's a charecter")
'''
#
'''
x = input("Enter it...")
if(x>='A' and 'Z'>=x):
    print("it's a upper case charecter")
elif('a'<=x<='z'):
    print("It's a lower case charecter")
elif(x>='0' and x<='9'):
    print("It's a digit")
else:
    print("It's a special charecter")
'''
# build multi-functional calculator with zero-division protection
x = int(input("Enter the number: "))
y = int(input("Enter the number: "))
opareter = input("chose the opareter (+,-,*,/,%):-")
if(opareter == '+'):
    print(f"{x} + {y} = ",x+y)
elif(opareter == '-'):
    print(f"{x} - {y} = ",x-y)
elif(opareter == '*'):
    print(f"{x} * {y} = ",x*y)
elif(opareter == '/'):
    if(y!=0):
        print(f"{x} / {y} = ",x/y)
    else:
        print("please enter a valid input")
elif(opareter == '%'):
    print(f"{x} % {y} = ",x%y)
else:
    print("please chose between +,-,*,/,%")