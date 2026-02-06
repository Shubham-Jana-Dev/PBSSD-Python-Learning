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
#a = int(input("Enter the number: "))  # use a float value for better understing (for creating the ValueError)
#b = int(input("Enter the number: "))
#print(f"{a} + {b} = ",a+b)


def order_something(customer_name,type_of_order, color= None):
    print(f"{customer_name} ordered {type_of_order}.")
    if color != None:
        print(f"color : {color}\n") 
# order_something("Shubham","Coffee","Black")
# order_something("Sinchen","Ice-cream","chocolet")
# order_something("Sinchen","tost","momo","tomato sos")


def understanding_args(customer_name,type_of_order,*args):
    print(f"{customer_name} has ordered {type_of_order} ")
    for i in args:
        print("Add + ",i)
# understanding_args("Sinchen","tost","momo","tomato sos","with extra chili flex")
# understanding_args("Shubham","Coffee")


def understanding_dubble_star_kwargs(customer_name,type_of_order,**kwargs):
    print(customer_name,type_of_order)
    for key,value in kwargs.items():
        print("ADD + ",key,":",value)
# understanding_dubble_star_kwargs("Shubham","burger",seeetener="Mihi dana",drinks="Orange juice")


def understanding_both_at_once_implementation(customer_name,type_of_order,*args,**kwargs):
    print(customer_name," ordered ",type_of_order)
    for key,value in kwargs.items():
        print("Add - ",key,":",value)
    for i in args:
        print("also Add : ",i)
#understanding_both_at_once_implementation("Shubham","burger","Mihi dana",drinks="Orange juice")

# exporing the unpacking the *agr and **kwargs
shubhams_extra_order = ("rice cake","Lemon rice")
lilis_extra_order = ("green tea","lemon","suger")
shubhams_extra_orderkw = { "drinks":"Orange juice", "sweetener" :"Gulab Jamun"}
# understanding_both_at_once_implementation("Shubham","Burger",*shubhams_extra_order,**shubhams_extra_orderkw)
# understanding_both_at_once_implementation("Lili","Pizza",*lilis_extra_order)
'''
​The "Smart Billing" Challenge:
Modify your understanding_both_at_once_implementation function to calculate a Total Bill.
​Pass a list of items using *args.
​Pass their prices using **kwargs.
​The Twist: If an item in args matches a key in kwargs, add its price to the total. If it
doesn't match, print "Price missing for [Item]".
​Example Input: smart_bill("Shubham", "Dinner", "Burger", "Pizza", Burger=120, Pizza=250, Coke=50)
'''
def smart_bill(*args,**kwargs):
    sum = 0
    for key,value in kwargs.items():
        for arg in args:
            if arg == key:
                if arg == "Shubham" and arg == "Dinner":
                    continue
                else:
                    print(f"Price missing for {arg}")
        sum += value
    print(sum)
# smart_bill("Shubham", "Dinner", "Burger", "Pizza", Burger=120, Pizza=250, Coke=50)

# has fullfill the reqirment...
def smart_bill1(*args,**kwargs):
    TotalSum = 0
    for i in args:
        if i in kwargs:
            TotalSum += kwargs[i]
        else:
            print(f"Price missing for {i}")
    print(TotalSum)
# smart_bill1("Shubham", "Dinner", "Burger", "Pizza", Burger=120, Pizza=250, Coke=50)


