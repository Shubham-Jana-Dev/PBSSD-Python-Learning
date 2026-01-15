# 1. Print the factorial of all numbers between a range.
"""
x = int(input("Enter the first range: "))
y = int(input("Enter the last range: "))
if x<y:
    for i in range(x,y+1):
        temp = i
        fact = 1
        while temp != 0:
            fact = fact*temp
            temp = temp - 1
        print(f" The factorial of {i} = {fact}.")
else:
    print("Please enter the valid order.")
"""
# 2. Reverse all the numbers between a Particular range
num1 = int(input("Enter the first range: "))
num2 = int(input("Enter the last range: "))
for i in range(num1,num2 + 1):
    temp = i
    rev = 0
    while temp != 0:
        rem = temp%10
        rev = (rev * 10) + rem
        temp //= 10
    print(f"The reverse number of {i} = ",rev)
