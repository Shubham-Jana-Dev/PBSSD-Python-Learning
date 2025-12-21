class raj:
    name = "Shubham Jana"
# print(name) invalid
print(raj.name)
print("01------------------------")
def add(): # Function declaration
    x = int(input("Enter the Number : "))
    y = int(input("Enter the Number : "))  #Function definition
    z = x+y
    print(z)
add()  # Function call
print("02------------------------")
x1 = int(input("Enter the Number : "))
y1 = int(input("Enter the Number : "))
z1 = x1+y1
def add2():
    x1 = int(input("Enter the Number : "))
    y1 = int(input("Enter the Number : "))
    z1 = x1+y1
add2()
print(x1)
print(y1)
print(z1)
print("03------------------------")
x2 = 100
y2 = 200
def add3():
    x2 = 600
    y2 = 500
    print(x2+y2)
add3()
print("04------------------------")
x3 = 100
y3 = 200
def add4():
    print(x3+y3)  # We can perform modification in the global variables inside the local block
add4()
print("05-Class-work-----------------------")
x4 = 1
y4 = 6
z4 = 10
x4 = x4 + y4 + z4
y4 = x4 + y4 + z4
z4 = x4 + y4 + z4 
x4 = y4 - x4
y4 = x4 - z4
z4 = x4 + y4 + z4
print(x4)
print(y4)
print(z4)
 
