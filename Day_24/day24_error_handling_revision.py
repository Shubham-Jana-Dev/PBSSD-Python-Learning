def division():
    try:
        numerator = float(input("Enter the numerator: "))
        denominator = float(input("Enter the denominator: "))
        quotient = numerator/denominator
        print(f"The quotient is {quotient}.")
    except ValueError:
        print("Please enter a valid input")
    except ZeroDivisionError:
        print("We can not divide aany number by Zero.")
division()