#1) How to Reverse a Number in Python
"""
num = int(input("Enter the number: "))
temp = num
rev_num = 0
while temp != 0:
    last_digit = temp%10
    rev_num = rev_num * 10 + last_digit
    temp //= 10
print(rev_num)
"""

# 2) Python Program to convert Number to Word (Mathematical Method)
'''
num = int(input("Enter the number: "))

# Handle the special case for 0 immediately
if num == 0:
    print("zero")
else:
    temp = num
    rev_num = 0
    original_digit_count = 0

    # STEP 1: Reverse the number and count digits
    while temp > 0:
        digit = temp % 10
        rev_num = (rev_num * 10) + digit
        temp //= 10
        original_digit_count += 1

    # STEP 2: Extract digits from reversed number and print
    processed_count = 0
    while processed_count < original_digit_count:
        # Get the last digit of the reversed number
        current_digit = rev_num % 10
        
        if current_digit == 0:
            print("zero")
        elif current_digit == 1:
            print("one")
        elif current_digit == 2:
            print("two")
        elif current_digit == 3:
            print("three")
        elif current_digit == 4:
            print("four")
        elif current_digit == 5:
            print("five")
        elif current_digit == 6:
            print("six")
        elif current_digit == 7:
            print("seven")
        elif current_digit == 8:
            print("eight")
        elif current_digit == 9:
            print("nine")

        # Prepare for next digit
        rev_num //= 10
        processed_count += 1
'''
# 3) Automorphic Number Program in python
"""
num = int(input("Enter the number: "))
temp = num
count = 0
sq = num**2
while temp != 0:
    temp  //= 10 
    count += 1
print(count)
div = 10**count
if sq%div == num:
    print("It's a Automorphic number")
else:
    print("It's not a Automorphic number")
"""
# 4) Peterson Number in python
'''
num = int(input("Enter the number: "))
temp = num
last_digit = 0
total_sum = 0

while temp>0:
    last_digit = temp%10
    f = 1
    fact = 1
    while f<=last_digit:
        fact = fact * f
        f += 1
    total_sum += fact
    temp //= 10
if total_sum == num:
    print("Peterson Number")
else:
    print("Not a Peterson Number")
'''
# 5) Sunny Number in python
"""
num = int(input("Enter the number: "))
n = num + 1
i =1
found = False
while i * i <= n:
    if i * i == n:
        found = True
    i += 1
if found:
    print(f"{num} is a sunny number.")
else:
    print(f"{num} is not a sunny number.")
"""
# OR, other method 
'''
count =0
for i in range (1,1001):
    n=i +1
    root =n **0.5
    rr = int(root)
    sq = rr**2
    if sq == n:
        count += 1
print(count)
'''
# 6) Tech Number in python
"""
num = int(input("Enter the number: "))
temp = num
count = 0
while temp != 0:
    temp //= 10
    count +=1

if count%2 == 0:
    spliter = 10**(count//2)
    left_half = num // spliter
    right_half = num % spliter
    total_sum = left_half + right_half
    if total_sum ** 2 == num:
        print(f"{num} is a tech number :)")
    else:
        print(f"{num} is not a tech number :(")
else:
    print(f"{num} has odd digits, so it cannot be a tech number.")
"""