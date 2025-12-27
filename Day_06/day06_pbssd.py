# Day 06: Complex Literals and Type Behavior
# Training: PBSSD Python Learning

print("------01------")
x = 10 + 20j
print(x, type(x))
print(x.real)
print(x.imag)
# LEARNING: Accessing .real and .imag always returns a float, even if defined as int.
print("------02------")
x = 10 + 23j
a = x.real
b = x.imag
print(a, type(a))
print(b, type(b))
# LEARNING: Confirms that individual components of a complex number belong to the 'float' class.
print("------03------")
x = complex()
print(x)
# LEARNING: Calling complex() without arguments creates 0j (the default complex value).
print("------04------")
x = 10
y = 30
z = complex(x, y)
print(z)
# LEARNING: You can create a complex number by passing two variables (real, imag) into the complex() constructor.
print("------05------")
# z = complex(input("Enter the value :- "))
# print(z)
print("COMMENT: This code is commented out because complex() constructor does not directly clean input strings with spaces.")
# WHY IT FAILS: complex() is strict about string formatting (no spaces around '+' or 'j').
print("------06------")
x = 10 + 30j
y = 30 + 80j
print(x + y)
print(x - y)
# LEARNING: Standard arithmetic (+ and -) works natively with complex objects.
print("------07------")
# (Repeat of example 06 - practicing consistency in operations)
print(x + y)
print(x - y)
print("------08------")
x = 1 + 3j
y = 3 + 4j
print(x * y)
print(x / y)
# print(x // y)
# WHY IT FAILS: Floor division (//) is NOT allowed for complex numbers because 'imaginary' values cannot be floored.
print("------09------")
x = complex("12")
print(x)
# LEARNING: Passing a single string "12" creates 12+0j.
print("------10------")
print("COMMENT: Commented out because complex() only takes TWO numeric arguments, or ONE string argument.")
'''
x = complex("12","45") # FAILS: Cannot take two strings.
x = complex(12,"45")   # FAILS: Second argument cannot be a string if first is numeric.
x = complex("12",45)   # FAILS: First argument cannot be a string if second is numeric.
'''




