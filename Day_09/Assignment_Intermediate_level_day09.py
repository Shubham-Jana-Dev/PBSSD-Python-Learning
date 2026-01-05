#31 Find out the leargest number between two numbers.
"""
a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))
if a>b:
    print(f"{a} is largest.")
else:
    print(f"{b} is largest.")
"""
#32. Find the smallest of two numbers.
'''
a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))
if a<b:
    print(f"{a} is smallest.")
else:
    print(f"{b} is smallest.")
'''
#33. Find the largest of three numbers.
"""
a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))
c = float(input("Enter the third number: "))
if (a>=b and a>=c) :
    print(f"{a} is largest.")
elif (b>=c):
    print(f"{b} is largest.")
else:
    print(f"{c} is largest.")
"""
#34. Find the smallest of three numbers.
'''
a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))
c = float(input("Enter the third number: "))
if (a<=b and a<=c) :
    print(f"{a} is smallest.")
elif (b<=c):
    print(f"{b} is smallest.")
else:
    print(f"{c} is smallest.")
'''
#35. Check whether a number is a 3-digit number.
num = int(input("Enter the number: "))
if(99<num<1000) or (-999<=num<=-100):
    print("Yes it's a 3-digit number.")
else:
    print("It's not a 3-digit number.")