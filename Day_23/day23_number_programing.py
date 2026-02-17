# Write a program to i dentify the prime number.
def prime_numbers(num):
    for i in range(2,num):
        if num%i == 0:
            print("This is not a prime number.")
            break
    else:
        print("This is a prime number.")
# num = int(input("Enter the number: "))
# prime_numbers(num)

# Print all digits of a number.
def print_digits(num):
    temp = num
    length = len(str(temp))
    while temp != 0:
        rem = temp%10
        print(rem)
        temp //= 10
# print_digits(3432)

# Reverse a Number 
def reverse_number(num):
    temp = num
    rev = 0
    length = len(str(num))
    while temp != 0:
        last_digit = temp%10
        rev = rev*10+last_digit
        temp//=10
    return rev
    # print(f"The reversed number is {rev}.")
# reverse_number(22156)

# Check a number is a palindrome number or not.
def check_palindrome(num):
    if num == reverse_number(num):
        print(f"{num} is a palindrome number.")
    else: 
        print(f"{num} is not a palindrome number.")
# check_palindrome(1221)

# The raw method

def palindrome(num):
    temp = num
    reverse = 0
    while temp != 0:
        last_digit = temp%10
        reverse = reverse*10+last_digit
        temp//=10
    if num == reverse:
        print(f"{num} is a palindrome number.")
    else:
        print(f"{num} is not a palindrome number")
# palindrome(19031)

# Check a mstrong number is an Amstrong number is not.
def armstrong(num):
    temp = num
    power = 0
    length = len(str(temp))
    while temp != 0:
        last_digit = temp%10
        power = power + last_digit**length
        temp //= 10
    if power == num:
        print(f"{num} is an amstrong number.")
    else:
        print(f"{num} is not an amstrong number.")
armstrong(370)