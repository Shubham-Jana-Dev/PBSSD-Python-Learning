x = int(input("Enter start value (x): "))
y = int(input("Enter end value (y): "))

no_even = 0; no_odd = 0; sum_even = 0; sum_odd = 0

while x <= y:  
    if x % 2 == 0:
        print("Even number = ", x)
        no_even += 1
        sum_even += x
    else:
        print("Odd number = ", x)
        no_odd += 1
        sum_odd += x
    x += 1  
print(f"Total Even: {no_even}, Sum: {sum_even}")
print(f"Total Odd: {no_odd}, Sum: {sum_odd}")


x = int(input("Enter the number: "))
fact = 1
temp = x
while temp > 0:
    fact *= temp
    temp -= 1
print(f"The factorial of {x} is {fact}")