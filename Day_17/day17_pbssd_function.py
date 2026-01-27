# understand high order functions like filter(),map()
def understand_higher_order_fun():
    nums_list = [2,4,6,3,5,77,6,12]
    p = list(map(lambda num: num**3,nums_list))  # cube all numbers of the list
    print(p)
    even_only = list(filter(lambda num : num%2 == 0,p))   # it would help to fillter out the odd numbers
    print(even_only)
    # return p , even_only
understand_higher_order_fun()