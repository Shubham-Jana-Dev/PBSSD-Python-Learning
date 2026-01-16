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
'''
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
'''
# Class work 3 :- Write a program to print all palindrom numbers
"""
x = int(input("Enter the first range: "))
y = int(input("Enter the last range: "))
if x<y:
    for i in range(x,y+1):
        temp = i
        rev = 0
        while(temp !=0):
            rem = temp%10
            rev = rev * 10 + rem
            temp //=10
            if( rev == i):
                print(i) 
"""
# Check a number is amstrong numbner or not.
num = int(input("Enter the number: "))
temp = num 
temp1 = num
length =0
total_sum =0
while (temp !=0):
    rem = temp%10
    length += 1
    temp //= 10
while (temp1 !=0):
    rem1 = temp1%10
    total_sum += (rem1**length)
    temp1 //=10
if(total_sum == num):
    print(f"{num} is an amstrong number.")
else:
    print(f"{num} is not an amstrong number.")
# class work 4 :- Write a program to print all amstrong numbers between a range
num1 = int(input("Enter the starting range: "))
num2 = int(input("Enter the ending range: "))
temp = 1
if(num1<num2):
    for i in range(num1,num2+1):
        temp1 = i
        temp2 = i
        length = 0 
        total_sum =0
        while(temp1 !=0):
            rem=temp1%10
            length +=1
            temp1 //= 10
        while(temp2 != 0):
            rem2 = temp2%10
            total_sum += (rem2**length)
            temp2 //= 10
        if(total_sum == i):
            print(i)

    