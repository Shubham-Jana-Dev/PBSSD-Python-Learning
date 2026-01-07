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
'''
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
'''
'''
Calculate the electric bill amount-
0 unit --> 15 unit = ₹6.20/unit
15 unit --> 40 unit = ₹8.01/unit
20 unit --> 25 unit = ₹9.75/unit
30 unit --> 80 unit = ₹21.71/unit
80 unit --> 120 unit = ₹45.47/unit
90 unit --> 200 unit = ₹96.00/unit
>200 unit = ₹98.77/unit
'''
unit = float(input("Enter the unit of the electricity uses :- "))
if(0<=unit<=15):
    print("Your bill: ₹",unit*6.20)
elif(15<unit<=40):
    if(20<unit<=25):
        print("Your bill: ₹",unit*9.75)
    elif(30<unit<=40):
        print("Your bill: ₹",unit*21.71)
    else:
        print("Your bill: ₹",unit*8.01)
elif(40<unit<=80):
    print("Your bill: ₹",unit*21.71)
elif(80<unit<=120):
    if(90<unit<=120):
        print("Your bill: ₹",unit*96.00)
    else:
        print("Your bill: ₹",unit*45.47)
elif(120<unit<=200):
    print("Your bill: ₹",unit*96.00)
elif(200<unit):
    print("Your bill: ₹",unit*98.77)
else:
    print("Please enter a valid input.")
    