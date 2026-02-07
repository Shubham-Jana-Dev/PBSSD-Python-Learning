'''
Write a function called average_score that calculates the average of an arbitrary number of scores.
Sample output
average_score(85, 90, 78) -> 84.333...
average_score(100, 95) -> 97.5
average_score() -> 0
'''
def average_score(*args):
    num = 0
    hold = 0
    for i in args:
        num += 1
        hold +=i
    if num == 0 :
        print(0)
    else:
        e = hold/num
        print(e)
# average_score(85,90,78)
# average_score(100,95)
# average_score()
def more_pythonic(*args):
    if not args:
        return 0
    return sum(args)/len(args)
more_pythonic(85,90,78)
more_pythonic(100,95)
more_pythonic()

'''
Write a function describe_pet that accepts a pet’s name and type as required arguments, but can also take any number of keyword details.

Sample output:-

Pet name: Whiskers
Animal type: cat
Details:
  color: gray
  age: 3
  favorite_food: tuna
'''
# TODO write the describe_pet function

# Example usage:
def describe_pet(*args,**kwargs):
    print("Name: ",args[0],"\nAnimal Type: ",args[1])
    print("Details: ")
    for i in kwargs:
        print(" ",i,":",kwargs[i])
# describe_pet("Whiskers", "cat", color="gray", age=3, favorite_food="tuna")


# in another way to solve this 
# Example usage:
def describe_pet(name,animal,**kwargs):
    print(f"Name: {name}\nanimal Type: {animal}")
    print("Details: ")
    for i in kwargs:
        print(f"{i}: {kwargs[i]}")
describe_pet("Whiskers", "cat", color="gray", age=3, favorite_food="tuna")

'''
Write a function describe_pet that accepts a pet’s name and type as required arguments, but can also take any number of keyword details.

Sample output:-

Pet name: Whiskers
Animal type: cat
Details:
  color: gray
  age: 3
  favorite_food: tuna
'''
# TODO write the describe_pet function

"""
The "Inventory Manager" Challenge
Let's combine everything you've learned into a mini-project. This will test your *args, **kwargs, and loop skills at once.

The Goal: Write a function manage_inventory that:
Takes a store_name as a required argument.
Takes any number of items as *args.
Takes stock_counts as **kwargs.
The Logic: For every item in the list (args), print how many are in stock from the dictionary (kwargs). If it's not in the dictionary, print "Out of stock."
Example Call: manage_inventory("TechShop", "Laptop", "Mouse", "Monitor", Laptop=10, Mouse=5)

Expected Output:

Plaintext
Inventory for TechShop:
Laptop: 10 in stock
Mouse: 5 in stock
Monitor: Out of stock
"""
def manage_inventory(shop_name,*args,**kwargs):
    print(f"Inventory for {shop_name}:")
    for item in args:
        if item in kwargs:
            print(f"{item}: {kwargs[item]} in stock")
        else:
            print(f"{item}: out of stock")
manage_inventory("TechShop", "Laptop", "Mouse", "Monitor", Laptop=10, Mouse=5)
