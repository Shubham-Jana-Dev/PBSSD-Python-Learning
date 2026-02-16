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