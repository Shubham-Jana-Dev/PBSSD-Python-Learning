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
# more_pythonic(85,90,78)
# more_pythonic(100,95)
# more_pythonic()

'''
Write a function describe_pet that accepts a pet’s name and type as required arguments, but can also take
 any number of keyword details.

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
# describe_pet("Whiskers", "cat", color="gray", age=3, favorite_food="tuna")

'''
Write a function describe_pet that accepts a pet’s name and type as required arguments, but can also take any number 
of keyword details.

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
The Logic: For every item in the list (args), print how many are in stock from the dictionary (kwargs). If it's not in the 
dictionary, print "Out of stock."
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
# manage_inventory("TechShop", "Laptop", "Mouse", "Monitor", Laptop=10, Mouse=5)
"""
The Challenge: The VIP Guest List 🎟️
The Goal: Write a function called check_guests that separates "VIP" guests from "Regular" guests and calculates the total entry fee.

The Rules:
Required Argument: min_age (an integer).
Flexible Arguments (*args): A list of guest names.
Keyword Arguments (**kwargs): Guest names as keys and their ages as values.
The Logic:
For every name in args:
Check their age in **kwargs.
If their age is greater than or equal to min_age, print: "[Name] is invited."
If their age is less than min_age OR their name isn't in kwargs, print: "[Name] is NOT invited."
The Twist: If a guest is invited AND their age is 50 or above, they are a VIP (print "[Name] is a VIP!").
Example Input:
Python
check_guests(21, "Shubham", "Rohan", "Amit", Shubham=25, Rohan=19, Amit=55)
Expected Output:
Plaintext
Shubham is invited.
Rohan is NOT invited.
Amit is invited.
Amit is a VIP!
"""
def check_guests(age,*args,**kwargs):
    for i in args:
        if i in kwargs:
            if kwargs[i] >= age:
                print(f"{i} is invited.")
                if kwargs[i] >=50:
                    print(f"{i} is a VIP!")
            else:
                print(f"{i} is NOT invited.")

# check_guests(21, "Shubham", "Rohan", "Amit", Shubham=25, Rohan=19, Amit=55)

"""
Problem 3

Write a function make_sandwich that accepts any number of ingredients and any number of optional preferences.

Sample output

Making a sandwich with:
  turkey
  lettuce
  tomato
Options:
  sauce: mayo
  toasted: True
 
[ ]
# TODO Write the make_sandwich function# Example usage:make_sandwich("turkey", "lettuce", "tomato", sauce="mayo", toasted=True)
"""
def make_sandwich(*args,**kwargs):
    print("Making a sandwich with: ")
    for i in args:
        print(f"  {i}")
    print("Options: ")
    for i in kwargs:
        print(f"  {i}: {kwargs[i]}")
# make_sandwich("turkey", "lettuce", "tomato", sauce="mayo", toasted=True)

"""
The "Kitchen Safety" Logic Challenge 🍳
The Goal: Modify (or write a new version of) make_sandwich to include Validation.

The New Rules:
The Forbidden Ingredient: If "Pineapple" is in the args, print: "Error: We don't put pineapple on sandwiches!" and stop the function immediately (don't print anything else).
The "Toasted" Check: If toasted=True is in the kwargs, add a message at the very end saying: "* Carefully, it's hot! *"
The "Empty" Order: If the user calls make_sandwich() with no ingredients, print: "You can't make a sandwich with nothing!"
"""
def smart_sandwich_maker(*args,**kwargs):
    bad_items = ""
    pp = ("turkey", "lettuce", "tomato", "cheese", "ham", "bread")
    flag = 1
    if not args:
        print("You can't make a sandwich with nothing!")
        return 
    for i in args:
        if i == "Pineapple" or i == "pineapple": # i could use i.lower() but i didn't avoiding the build-in fuction.
            print("Error: We don't put pineapple on sandwiches!")
            return
        if i not in  pp:
            print(f"Error: {i} is not edible! We are a restaurant, not a hardware store.")
            return        
    else:  
        print("Making a sandwich with:")
        for i in args:
            print(f"  {i}")
    if kwargs.get("toasted") == True:
        print ("* Carefully, it's hot! *")
        return 
    
smart_sandwich_maker("tomato", "cheese", "phone", "ham", "bread", )
