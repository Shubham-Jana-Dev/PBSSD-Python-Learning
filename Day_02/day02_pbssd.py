''' Python Identifiers '''

name = "Shubham Jana"
x = 123
# A%B = 125 it will return Error  Rule 1.1 & 1.2
print("-------------------------------")
'''Case Sensitive'''
Name = "Shubham"
name = "jana"
print(Name)
print(name)  # Rule 1.3
print("-------------------------------")
'''Digit rule'''
variable1 = 100 #It's correct
# 1variable = 123 It's not correct when we run the it will be return error
print("-------------------------------")
'''No spaces rule'''
# my name = "Shubham Jana" It's not correct when we run it, it will be returned Rule
my_name = "Shubham Jana"
my_name_is = "Raj" # We can use multiple '_' in a variable name
print(my_name) #Rule 1.4
_ = "Shubham" #We can use a single '_' In variable name
print("-------------------------------")
'''Reserved keywords rule'''
# if = 333 It's not correct when we run it, it will be returned Road
print("-------------------------------")
'''Built in function for character conversion'''
print(ord('A'))  # ord()
print(ord('&'))
print(ord('9'))
print("-------------------------------")
print(str('65'))  # str()
print(str('10'))
print(str('95'))
print("-------------------------------")
'''Single Value Assignment'''
x = 100
y = 200
print(id(x))
print(id(y))
print("-------------------------------")
'''Multi variable single value assignment'''
x = y = z = 122
print(id(x))
print(id(y))
print(id(z))
print("-------------------------------")
'''Corresponding value assignment'''
x,y,z = 100,300,45
print(id(x))
print(id(y))
print(id(z))
print("-------------------------------")
'''Getting input from the user Via keyboard'''
name = input("Enter the name: ")
age = input("Enter the age: ")
print(type(name))
print(type(age))
