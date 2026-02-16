# Write a program to i dentify the prime number.
def prime_numbers(num):
    for i in range(2,num):
        if num%i == 0:
            print("This is not a prime number.")
            break
    else:
        print("This is a prime number.")
num = int(input("Enter the number: "))
prime_numbers(num)