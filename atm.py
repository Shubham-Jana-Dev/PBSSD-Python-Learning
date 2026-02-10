#ATM Simulation

# def withdrow(balance,amount):
#     if amount <= balance:
#         return balance - amount
#     else:
#         print("Insufficient balance")
#         return
# import atm
# balance = 50000
# print(atm.withdrow(balance,1200))

# # from atm import withdraw
# balance = 5000
# print(withdraw(balance,1200))

def student(marks):
    if 100 >= marks >= 40 :
        print("PASS ")
        return
    elif 40 > marks >= 0:
        print("FAIL ")
        return
    else:
        print("Invalid input!")
student(45)