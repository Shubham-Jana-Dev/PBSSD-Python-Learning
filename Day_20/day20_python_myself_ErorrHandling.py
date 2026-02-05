def NameErrorHandling():
    try:
        a = o
        b = 23
        print(a + b)
    except NameError:
        print("Invalid input. :( \n ! Please enter a valid input for a and b. :) ")
NameErrorHandling()