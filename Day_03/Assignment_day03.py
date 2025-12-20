# 1. find out the area of parallelogram by python Script.
# formula, Area = base X hight
'''
base = float(input("Enter the value of the base : "))
height = float(input("Enter the value of the height : "))
area = base*height
print("The area of the parallelogram is ",area)
'''
# 2. Find out the area of conical vessel by python Script.
'''
r = float(input("Enter the value of redius : "))
h = float(input("Enter the value of vertical height : "))
l = ((r*r)+(h*h))**(1/2)
area = 3.14*r*(l+r)
print("The area of the conical vessel is ",area)
'''
# 3. find out the area of parallelepiped by python script.
"""
a = float(input("Enter the first side (a): "))
b = float(input("Enter the second side (b): "))
h = float(input("Enter the height(h) : "))
face1 = a*b
face2 = b*h
face3 = h*a
area = 2*(face1 + face2 + face3)
print("The total surface area is ",area)
"""
# 4. Solve quadratic equation by python script.
'''
a = float(input("Enter a : "))
b = float(input("Enter b : "))
c = float(input("Enter c : "))
d = (b*b)-(4*a*c)
root1 = (-b+(d**0.5))/(2*a)
root2 = (-b-(d**0.5))/(2*a)
print("Solution 1 : ",root1)
print("Solution 2 : ",root2)
''' 
# 5. Find the area of equilateral triangle by using Python script.
'''
h = float(input("Enter the value of height "))
area = (h*h)/(3**0.5)
print("The area of the equilateral triangle is ", area)
'''
# 6. Find out the area of a ellipse by using Python script.
'''
a = float(input("Enter the value of semi-major axis: "))
b = float(input("Enter the value of semi-minor axis: "))
area = 3.14*a*b
print("The area of the ellipse is : ", area )
'''
# 7. Convert kilometre to miles by using Python script.
"""
k = float(input("Enter Kilometre : "))
m = k * 0.6214
print(m) 
"""
# 8. Check a triangle is right angle triangle or not without conditional statement by using Python script.
'''
a = float(input("Enter the shortest side : "))
b = float(input("Enter the middle side : "))
c = float(input("Enter the longest side : "))
is_right_angle = (a*a + b*b) == (c*c)
print("Is this a right-angled triangle?",is_right_angle)
'''
# 9. Convert temperature from centigrade to Fahrenheit or Kelvin in Python script.
'''
c= float(input("Enter the value of temperature in centigrade : "))
f= (c*1.8)+32
k = c+273.15
print("in fahrenheit : ",f)
print("in kelvin : ",k)
'''
# 10. Find out the area of a rhombus and hub circle by using Python script.
'''
d1 = float(input("enter the fast diagonal of the rhombus"))
d2 = float(input("enter the second diagonal of the rhombus"))
r = float(input("enter the radius of the circle"))
area1 =(d1*d2)/4
area2 = (3.14*(r*r))/2
print("the area of the half Rhombus is",area1)
print("the area of the half circle is",area2)
'''
# 11. Find out the total surface area of a cube in Python script.
s = float(input("Enter the side "))
area = 6*(s*s)
print("The total area is ",area)
