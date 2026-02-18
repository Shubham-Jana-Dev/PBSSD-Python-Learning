#31 Find out the leargest number between two numbers.
def problem_31():
    a = float(input("Enter the first number: "))
    b = float(input("Enter the second number: "))
    if a>b:
        print(f"{a} is largest.")
    else:
        print(f"{b} is largest.")
# problem_31()

#32. Find the smallest of two numbers.
def problem_32():
    a = float(input("Enter the first number: "))
    b = float(input("Enter the second number: "))
    if a<b:
        print(f"{a} is smallest.")
    else:
        print(f"{b} is smallest.")
# problem_32()

#33. Find the largest of three numbers.
def problem_33():
    a = float(input("Enter the first number: "))
    b = float(input("Enter the second number: "))
    c = float(input("Enter the third number: "))
    if (a>=b and a>=c) :
        print(f"{a} is largest.")
    elif (b>=c):
        print(f"{b} is largest.")
    else:
        print(f"{c} is largest.")
# problem_33

#34. Find the smallest of three numbers.
def problem_34():
    a = float(input("Enter the first number: "))
    b = float(input("Enter the second number: "))
    c = float(input("Enter the third number: "))
    if (a<=b and a<=c) :
        print(f"{a} is smallest.")
    elif (b<=c):
        print(f"{b} is smallest.")
    else:
        print(f"{c} is smallest.")
# problem_34()
#35. Check whether a number is a 3-digit number.
def problem_35():
    num = int(input("Enter the number: "))
    if(99<num<1000) or (-999<=num<=-100):
        print("Yes it's a 3-digit number.")
    else:
        print("It's not a 3-digit number.")
# problem_35()
#36. Check whether a number is divisible by 3 and 5.
def problem_36():
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
# problem_36()

#37. Check whether a year is a century year.
def problem_37():
    y = int(input("Enter the year: "))
    if(y%100 == 0):
        print(f"{y} is a century year.")
    else:
        print(f"{y} is not a century year.")
# problem_37()

#38. Check whether a number is positive, negative, or zero.
def problem_38():
    num = float(input("Enter the number: "))
    if (num>0):
        print(f"{num} is a positive number.")
    elif(num<0):
        print(f"{num} is a negative number.")
    else:
        print(f"{num} is zero.")
# problem_38()

#39. Check whether a character is vowel, consonant, or not an alphabet.
def problem_39():
    char = input("Enter the character")
    if (char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u') or (char == 'A' or char == 'E' or char == 'I' or char == 'O' or char == 'U'):
        print(f"{char} is a vowel.")
    elif('a'<char<='z' or 'A'<char<='Z'):
        print(f"{char} is a consonant.")
    else:
        print(f"{char} is not a alphabet.")
# problem_39()

#40. Check whether a student passed or failed (pass mark = 40).
def problem_40():
        m = float(input("Enter your marks : "))
        if(0<=m<40):
            print("Failed :(")
        elif(m<=100):
            print("Passed :)")
        else:
            print("Please enter your valid marks")
# problem_40()

#41. Assign grade based on marks (A+,A, B, C, D, Fail).
def problem_41():
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
# problem_41()

#42. Check whether a triangle is valid based on angles.
def problem_42():
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
# problem_42()

#43. Check whether a triangle is equilateral, isosceles, or scalene.
def problem_43():
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
# problem_43()

#44. Check whether a number is divisible by 2, 3, or both.
def problem_44():
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
# problem_44()

#45. Calculate bonus:
# Salary ≥ 50000 → 10%
# Salary < 50000 → 5%
def problem_45():
    s = float(input("Enter your salary: "))
    if(0<=s<50000):
        print("Your bonus: ",s*0.05)
    elif(s>=50000):
        print("Your bonus: ",s*0.1)
    else:
        print("Salary must be positive.")
# problem_45()

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
# problem_49()

# 50.  Determine electricity bill category based on units consumed.
def problem_50():
    unit = int(input("Enter your unit consumed: "))
    category = int(input("""---Select your category---
    Enter '1' for General/EWS and Domestic category.
    Enter '2' for SC/ST/OBC and Domestic category.
    Enter '3' for Commercial category.
    Enter '4' for Industrial category
    ------------------------------------------------------
    Enter the category number here: """))
    if 0<category<5:
        if 0 <= unit <= 75:
            if category == 1 or category == 2:
                print("BILL FREE :) \n your bill amount is ₹ 0.00 /-")
            elif category == 3:
                print("TOTAL BILL \n your bill amount is ₹ %d /-",unit*0.15)
            else:
                print("TOTAL BILL \n your bill amount is ₹ ",unit*0.25,"/-")
        elif unit <= 100:
            if category == 1:
                print("TOTAL BILL \n your bill amount is ₹ ",unit*0.10,"/-")
            elif category == 2:
                print("BILL FREE :) \n your bill amount is ₹ 0.00 /-")
            elif category == 3:
                print("TOTAL BILL \n your bill amount is ₹ ",unit*0.20,"/-")
            else:
                print("TOTAL BILL \n your bill amount is ₹ ",unit*0.27,"/-")
        elif unit <= 150:
            if category == 1:
                print("TOTAL BILL \n your bill amount is ₹ ",unit*0.15,"/-")
            elif category == 2:
                print("TOTAL BILL \n your bill amount is ₹ ",unit*0.05,"/-")
            elif category == 3:
                print("TOTAL BILL \n your bill amount is ₹ ",unit*0.23,"/-")
            else:
                print("TOTAL BILL \n your bill amount is ₹ ",unit*0.30,"/-")
        elif unit <= 200:
            if category == 1:
                print("TOTAL BILL \n your bill amount is ₹ ",unit*0.18,"/-")
            elif category == 2:
                print("TOTAL BILL \n your bill amount is ₹ ",unit*0.08,"/-")
            elif category == 3:
                print("TOTAL BILL \n your bill amount is ₹ ",unit*0.25,"/-")
            else:
                print("TOTAL BILL \n your bill amount is ₹ ",unit*0.35,"/-")
        elif unit <= 200:
            if category == 1:
                print("TOTAL BILL \n your bill amount is ₹ ",unit*0.20,"/-")
            elif category == 2:
                print("TOTAL BILL \n your bill amount is ₹ ",unit*0.10,"/-")
            elif category == 3:
                print("TOTAL BILL \n your bill amount is ₹ ",unit*0.29,"/-")
            else:
                print("TOTAL BILL \n your bill amount is ₹ ",unit*0.40,"/-")
        elif unit > 200:
            if category == 1:
                print("TOTAL BILL \n your bill amount is ₹ ",unit*0.25,"/-")
            elif category == 2:
                print("TOTAL BILL \n your bill amount is ₹ ",unit*0.11,"/-")
            elif category == 3:
                print("TOTAL BILL \n your bill amount is ₹ ",unit*0.32,"/-")
            else:
                print("TOTAL BILL \n your bill amount is ₹ ",unit*0.45,"/-")
        else:
            print("Please enter a valid unit.... :(")
    else:
        print("Please enter a valid Category number.... :(")
# problem_50()

def problem_50_slab():
    unit = int(input("Enter units consumed: "))
    print("--- Select your category ---")
    print("1: General/EWS | 2: SC/ST/OBC | 3: Commercial | 4: Industrial")
    category = int(input("Enter category number: "))

    if not (1 <= category <= 4):
        print("Invalid Category!")
        return

    bill = 0.0
    remaining_units = unit

    # Slab 1: 0 - 75 units
    slab1 = min(remaining_units, 75)
    if category == 3: bill += slab1 * 0.15
    elif category == 4: bill += slab1 * 0.25
    # Categories 1 & 2 are free for this slab
    remaining_units -= slab1

    # Slab 2: 76 - 100 units (next 25 units)
    if remaining_units > 0:
        slab2 = min(remaining_units, 25)
        if category == 1: bill += slab2 * 0.10
        elif category == 3: bill += slab2 * 0.20
        elif category == 4: bill += slab2 * 0.27
        # Category 2 is still free here
        remaining_units -= slab2

    # Slab 3: 101 - 150 units (next 50 units)
    if remaining_units > 0:
        slab3 = min(remaining_units, 50)
        if category == 1: bill += slab3 * 0.15
        elif category == 2: bill += slab3 * 0.05
        elif category == 3: bill += slab3 * 0.23
        elif category == 4: bill += slab3 * 0.30
        remaining_units -= slab3

    # Slab 4: Above 150 units (simplified for this example)
    if remaining_units > 0:
        if category == 1: bill += remaining_units * 0.25
        elif category == 2: bill += remaining_units * 0.11
        elif category == 3: bill += remaining_units * 0.32
        elif category == 4: bill += remaining_units * 0.45

    if bill == 0:
        print("BILL FREE :) \nYour bill amount is ₹ 0.00 /-")
    else:
        print(f"TOTAL BILL \nYour bill amount is ₹ {bill:.2f} /-")

# problem_50_slab()
# 51. Find whether a given month has 30 or 31 days.
def problem_51():
    month = int(input("Enter the coresponding number of the month: "))
    if 0 < month <= 12:
        if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
            print(f"This month has 31 days.")
        else:
            print(f"This month has <30 days.")
    else:
        print("Please enter the valid id,")
# problem_51()
# 52. Find whether a character is uppercase 
# vowel, lowercase vowel, or consonant.
def problem_52():
    char = input("Enter a charecter: ")
    if 'A' <= char <= 'Z' or 'a' <= char <= 'z':
        if char == "A" or char == "E" or char == "I" or char == "O" or char == "U":
            print(f"{char} is a uper case vowel.")
        elif char == "a" or char == "e" or char == "i" or char == "o" or char == "u":
            print(f"{char} is a lower case vowel.")
        else:
            print(f"{char} is a consonant.")
    else:
        print("Please enter a valid input. :(")
# problem_52()
# 53. Check whether a number is a perfect square (logic-based).
def perfect_squre():
    num = int(input("Enter the number: "))
    root = num ** (0.5)
    int_r = int(root)
    squre_r = int_r*int_r
    if squre_r == num:
        print(f"{num} is a perfect squre number. :)")
    else:
        print(f"{num} is not a perfect squre number. :(")
    print(root)
    print(int_r)
    print(squre_r)
# perfect_squre()

# 54. Check whether a number is divisible by 10 and 5.
def problem_54():
    number = int(input("Enter the number: "))
    if number%10 == 0 and number%5 == 0 :
        print(f"{number} is divisible by 10 and 5.")
    else:
        print(f"{number} is not divisible by 10 and 5.")
problem_54()