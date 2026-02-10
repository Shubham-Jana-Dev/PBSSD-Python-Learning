import wallet
def amount(num1,num):
    if 0 <= num1 <= wallet.balance(num):
        return wallet.balance(num) - num1
    elif num1 > wallet.balance(num):
        return "Sorry insufficient Bank Balance."
    else:
        return "Please enter a valid input."

