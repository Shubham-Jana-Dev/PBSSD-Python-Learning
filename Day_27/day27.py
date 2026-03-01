My_list = [12,23,44,67,98,70,50,30,88]
blank = []
#print the elements which ade not divisible not the 
def using_loop():
    for i in My_list:
        if i%5 != 0:
            blank.append(i)
    print(blank)
# using_loop()

def by_list_comprehension():
    the_list = [i for i in My_list if i%5 !=0]
    print(the_list)
# by_list_comprehension()

# Find out the maximum element from a list.
def maximum_element():
    print(max(My_list))
# maximum_element()

# Find out the minimum element from a list.
def minimum_element():
    print(min(My_list))
# minimum_element()

# names = ['Shubham','Surajit','Arjun','Sneha','Karan','Sinchan','Doremon','Sisimanu'] filter out the name which starts with 'S' from the given list.
def filter_s_names():
    names = ['Shubham','Surajit','Arjun','Sneha','Karan','Sinchan','Doremon','Sisimanu']
    s_names = [n for n in names if 'S' in n]
    print(s_names)
filter_s_names()

