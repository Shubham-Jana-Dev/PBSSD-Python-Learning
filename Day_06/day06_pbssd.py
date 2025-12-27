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
