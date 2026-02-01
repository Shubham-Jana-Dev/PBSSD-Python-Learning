# understand high order functions like filter(),map()
def understand_higher_order_fun():
    nums_list = [2,4,6,3,5,77,6,12]
    p = list(map(lambda num: num**3,nums_list))  # cube all numbers of the list
    print(p)
    even_only = list(filter(lambda num : num%2 == 0,p))   # it would help to fillter out the odd numbers
    print(even_only)
    # return p , even_only
# understand_higher_order_fun()
def squre_number():
    num = int(input("Enter the number: "))
    x = lambda n : n*n
    print(f"The squre of the {num} is {x(num)}")
# squre_number()
def apply_operation(numbers, func):
    return[func(n) for n in numbers]
my_nums = [1,2,3,4,5,6]
squres = apply_operation(my_nums,lambda n : n**2)
cubes = apply_operation(my_nums, lambda n : n**3)
print("Squres : ",squres)
print("Cubes : ",cubes)


