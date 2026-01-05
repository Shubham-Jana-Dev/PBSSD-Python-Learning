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
""""""
m = float(input("Enter your marks : "))
if(0<=m<40):
    print("Failed :(")
elif(m<=100):
    print("Passed :)")
else:
    print("Please enter your valid marks")