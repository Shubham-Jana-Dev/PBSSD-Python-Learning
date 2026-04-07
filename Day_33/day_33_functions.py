# Write a function to calculate and return the square of a number.
def square(num):
    return num**2
#print(square(9))

# Create a function that takes two numbers as parameters and returns their sum.
def numbers_sum(num1,num2):
    return num1+num2
# print(numbers_sum(2,5))

# Write a function multiply that multiplies two numbers, but can also accept and multiply strings.
def multiply(number1,number2):
    return number1*number2
# print(multiply(3,"Shubham\n"))

# Create a function that returns both the area and circumference of a circle give its radius.
def area_and_circumference(radius):
    area = 3.14*(radius**2)
    circumference = 2*3.14*radius
    return area, circumference
a, c = area_and_circumference(2)
# print(f"Area = {a} \nCircumference = {c}")


# ********************************
# Write a function that greets a user. If no name is provided, it should greet with a defult name.
def greeting(name = "Shubham"):
        return "Hi, " + name
# print(greeting("Santosh"))
# print(greeting())
# ********************************

# ********************************
# Create a lambda function that returns the cube of a number
cube = lambda x: x**3
# print(cube(3))
# ********************************

# ********************************
# Write a function that takes variable number of arguments and returns their sum.
def the_sum(*args):
    return sum(args)
# print(the_sum(1,2,3,4))
# ********************************

# ********************************
# Create a function that accepts any number of keyword arguments and prints them in the format key: value.
def print_kwargs(**kwargs):
     for k,v in kwargs.items():
          print(f"{k} : {v}")
# print_kwargs(name = "Shubham", department = "B.tech in CSE", phone_number = 70099768321)


#
def greet(**kwargs):
     if kwargs:
          print(f"Hello {kwargs["name"]},{kwargs["msg"]}")
greet(name = "Shubham",msg ="Good morning")

#write a function to check whether number is odd or even?

def odd_even(num):
    if num%2 == 0:
        print("Even")
    else:
         print("Odd")
odd_even(3)

def large(a,b):
    if a>b:
         print(a)
    else:
         print(b)
large(2,5)

def all_sum(*args):
     print(sum(args))
all_sum(2,3,4,5,56,7)

def facto(num):
    if num == 0 or num == 1:
         return num
    else:
         return num*facto(num-1)
print(facto(5))

def rever(st):
     return st[::-1]
print(rever("Shubham"))

def count(st):
    v = 0
    for i in st:
         if i == 'a' or i == 'e' or i == 'o' or i == 'i' or i == 'u':
              v += 1
    return v
print(count("Shubham"))  
def pal(num):
    last_digit = num % 10
    first_digit = num // 100
    if (first_digit == last_digit):
        print("It's a palindrome number")
    else:
        print("It's not a palindrome number")
pal(121)

def prime_numbers(num):
    for i in range(2,num):
        if num%i == 0:
            print("This is not a prime number.")
            break
    else:
        print("This is a prime number.")
prime_numbers(1)

def all_sumq(*args):
    total = 0
    for i in args:
        total += i
    return total
print(all_sumq(1,2,3,4))