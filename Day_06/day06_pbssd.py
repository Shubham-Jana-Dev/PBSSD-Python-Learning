# Day 06: Complex Literals and Type Behavior
# Training: PBSSD Python Learning

print("------01------")
x = 10 + 20j
print(x, type(x))
print(x.real)
print(x.imag)
# LEARNING: Accessing .real and .imag always returns a float, even if defined as int.