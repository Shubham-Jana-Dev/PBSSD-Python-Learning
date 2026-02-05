def NameErrorHandling():
    try:
        a = o # I have use string (without " ") for creating the NameError.
        b = 23
        print(a + b)
    except NameError:
        print("Invalid input. :( \n ! Please enter a valid input for a and b. :) ")
# NameErrorHandling()


def ValueErrorHandling():
    try:
        a = int(input("Enter the number: "))  # use a float value for better understing (for creating the ValueError)
        b = int(input("Enter the number: "))
        print(f"{a} + {b} = ",a+b)
    except ValueError:
        print("Please Enter integer value. :(")
        ValueErrorHandling()
# ValueErrorHandling()
a = int(input("Enter the number: "))  # use a float value for better understing (for creating the ValueError)
b = int(input("Enter the number: "))
print(f"{a} + {b} = ",a+b)
