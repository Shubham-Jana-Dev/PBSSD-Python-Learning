# 1. Print the factorial of all numbers between a range.
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
