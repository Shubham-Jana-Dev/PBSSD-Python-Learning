def NameErrorHandling():
    try:
        a = o
        b = 23
        print(a + b)
    except NameError:
        print("Invalid input. :( \n ! Please enter a valid input for a and b. :) ")
# NameErrorHandling()


def ValueErrorHandling():
    try:
        a = int(input("Enter the number: "))
        b = int(input("Enter the number: "))
        print(f"{a} + {b} = ",a+b)
    except ValueError:
        print("Please Enter integer value. :(")
        ValueErrorHandling()
# ValueErrorHandling()

