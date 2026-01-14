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
# 2) python Program to convert Number to Word
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
