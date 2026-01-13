#1) How to Reverse a Number in Python
#"""
num = int(input("Enter the number: "))
temp = num
rev_num = 0
while temp != 0:
    last_digit = temp%10
    rev_num = rev_num * 10 + last_digit
    temp //= 10
print(rev_num)
#"""