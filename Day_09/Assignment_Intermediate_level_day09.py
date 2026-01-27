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
"""
num = int(input("Enter the number: "))
if(99<num<1000) or (-999<=num<=-100):
    print("Yes it's a 3-digit number.")
else:
    print("It's not a 3-digit number.")
"""
#36. Check whether a number is divisible by 3 and 5.
'''
num = int(input("Enter the number: "))
if (num%3 == 0):
    if(num%5 == 0):
        print(f"{num} is divisible by both 3 and 5.")
    else:
        print(f"{num} is only divisible by 3 not by 5.")
else:
    if(num%5 == 0):
        print(f"{num} is only divisible 5 not by 3.")
    else:
        print(f"{num} is not divisible by both 3 and 5.")
'''
#37. Check whether a year is a century year.
"""
y = int(input("Enter the year: "))
if(y%100 == 0):
    print(f"{y} is a century year.")
else:
    print(f"{y} is not a century year.")
"""
#38. Check whether a number is positive, negative, or zero.
'''
num = float(input("Enter the number: "))
if (num>0):
    print(f"{num} is a positive number.")
elif(num<0):
    print(f"{num} is a negative number.")
else:
    print(f"{num} is zero.")
'''
#39. Check whether a character is vowel, consonant, or not an alphabet.
'''
char = input("Enter the character")
if (char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u') or (char == 'A' or char == 'E' or char == 'I' or char == 'O' or char == 'U'):
    print(f"{char} is a vowel.")
elif('a'<char<='z' or 'A'<char<='Z'):
    print(f"{char} is a consonant.")
else:
    print(f"{char} is not a alphabet.")
'''
#40. Check whether a student passed or failed (pass mark = 40).
"""
m = float(input("Enter your marks : "))
if(0<=m<40):
    print("Failed :(")
elif(m<=100):
    print("Passed :)")
else:
    print("Please enter your valid marks")
"""
#41. Assign grade based on marks (A+,A, B, C, D, Fail).
'''
m = float(input("Enter your percentage fo total marks: "))
if(0<=m<=25):
    print("failed")
elif(m<=45):
    print("D")
elif(m<=50):
    print("C")
elif(m<=65):
    print("B")
elif(m<=80):
    print("A")
elif(m<=100):
    print("A+")
else:
    print("Please enter the valid percentage...")
'''
#42. Check whether a triangle is valid based on angles.
"""
an1 = float(input("Enter the value of the first angle: "))
an2 = float(input("Enter the value of the second angle: "))
an3 = float(input("Enter the value of the third angle: "))
if(an1>0 and an2>0 and an3>0):
    if(an1 + an2 + an3 == 180):
        print("The triangle is valid.")
    else:
        print("The triangle is not valid.")
else:
    print("Please enter valid value angle.")
"""
#43. Check whether a triangle is equilateral, isosceles, or scalene.
'''
s1 = float(input("Enter the value of the first side: "))
s2 = float(input("Enter the value of the second side: "))
s3 = float(input("Enter the value of the third side: "))
if(s1>0 and s2>0 and s3>0):
    if(s2 + s1 > s3 and  s2 + s3 > s1 and  s1 + s3 > s2):
        if(s1 == s2  == s3):
            print("It's a equilatral.")
        elif(s1 == s2  or s2 == s3  or s1 == s3 ):
            print("It's a isosceles.")
        else:
            print("It's a scalene.")
    else:
        print("These sides cannot form a triangle.")

else:
    print("Please enter valid inputs.")
'''
#44. Check whether a number is divisible by 2, 3, or both.
"""
num = int(input("Enter the number: "))
if(num%2 == 0):
    if(num%3 == 0):
        print(f"{num} is divisible by both 2 and 3.")
    else:
        print(f"{num} is only divisible by 2 not by 3.")
else:
    if(num%3 == 0):
        print(f"{num} is only divisible by 3 not by 2.")
    else:
        print(f"{num} is not divisible neither 3 nor 2.")
"""
#45. Calculate bonus:
# Salary ≥ 50000 → 10%
# Salary < 50000 → 5%
'''
s = float(input("Enter your salary: "))
if(0<=s<50000):
    print("Your bonus: ",s*0.05)
elif(s>=50000):
    print("Your bonus: ",s*0.1)
else:
    print("Salary must be positive.")
'''
# 46. Find whether a number lies between two given numbers.
def problem_46():
    ran1 = int(input("Enter the starting: "))
    ran2 = int(input("Enter the ending: "))
    num = int(input("Enter the number: "))
    if ran1<ran2:
        if ran1<=num<=ran2:
            print(f"{num} is lies between {ran1} and {ran2}.")
        else:
            print(f"{num} does not lie between {ran1} and {ran2}.")
    else:
        print("Please fix the order of the range.")
# problem_46()
# 47. Check whether a number is divisible by 8 or 12.
def divisibility_47():
    num = int(input("Enter the number: "))
    if num%12 == 0 and num%8 == 0:
        print(f"{num} is divisible by both 8 and 12.")
    elif num%8 == 0:
        print(f"{num} is divisible by 8.")
    elif num%12 == 0:
        print(f"{num} is divisible by 12.")
    else:
        print(f"{num} is divisible by neither 8 nor 12. ")
# divisibility_47()
# 48. Check whether a person is a child, teenager, or adult.
def problem_48():
    age = int(input("Enter your age: "))
    if(0<=age<=12):
        print("You are a child.")
    elif(12<age<18):
        print("You are a teenager.")
    elif(18<=age):
        print("You are an adult.")
    else:
        print(f"Sorry you have to wait {age*(-1)} years of see a minimum output till then enjoy in the Heaven.")
# problem_48()
# 49. Check whether a number is a multiple of 3 or 7.
def problem_49():
    num = int(input("Enter the number: "))
    if num%3 == 0 and num%7 == 0:
        print(f"{num} is a multiple of both 3 and 7.")
    elif num%3 == 0:
        print(f"{num} is a multiple of 3.")
    elif num%7 == 0:
        print(f"{num} is a multiple of 7.")
    else:
        print(f"{num} is not a multiple of 7 nor 3.")
problem_49()