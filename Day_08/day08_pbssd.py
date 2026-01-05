# Explicit type casting
x = 16.4
print(x,type(x))
y = int(x)
print(y,type(y))
# Explicit type casting of the complex numbers
c = 13 + 43j
print(c)
print(type(c))
z = x.real
print(z,type(z))
a = x.imag
print(a,type(a))

# but one thisng 
# c = int(x)
# it would not be Executed.
# Because we cannot type cast complex variable into integer without breaking it into real imaginary.