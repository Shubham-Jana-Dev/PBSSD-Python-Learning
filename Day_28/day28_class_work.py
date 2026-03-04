# Take a dynamic list from the user and swap the first and the last element of the list (within 1.5 min)
def print_f_l_element():
    a = []
    l = int(input("Length: "))
    for i in range(l):
        el = input("Element: ")
        a.append(el)
    a[0],a[-1]=a[-1],a[0]
    print(a)
# print_f_l_element()

# Find out the duplicate elements from a given list. (without using set)
def find_duplicate_element():
    the_lists = [1,3,2,5,2,4,8,7,9,8]
    blank = []
    dup = []
    for i in the_lists:
        if i not in blank:
            blank.append(i)
        else:
            dup.append(i)
    print(f"The list of the duplicates elements are {dup}.")
# find_duplicate_element() 

# check 2 given lists are identical or not. (with in 1 min)
def check_identical():
    A = [1,2,3,4,5,6,7]
    B = [1,2,3,4,5,6,7]
    if A == B:
        print("Identical")
    else:
        print("Not Ientical")
# check_identical()

# Find out the -ve values from a list and remove them from the list and create a new list for storing them.
def fillter_negative():
    Mlist = [12,2,-32,64,33,-43,45]
    n = [i for i in Mlist if i<0]
    Mlist = [j for j in Mlist if j>=0]
    print(Mlist,'\n',n)
# fillter_negative()

# Take a list from the user and perfrom multiplication of all the integers, Addison of all the protein point numbers and continuation for all the strings. (15 minutes.)
def operation_according_data_type():
    he = []
    blank =[]
    length = int(input("Enter length: "))
    m = 1
    f = 0
    for i in range(length):
        chose = input("pleas chose the datatype (int, float, string): ")
        if chose == 'int':
            x = int(input("Enter the int:- "))
            m *= x
        elif chose == 'float':

            x = float(input("Enter the float:- "))
            f += x
        else:
            x = input("Enter the string:- ")
            blank.append(x)
            b ="".join(blank)
    if m != 1:
        print(m)
    if f != 0:
        print(f)
    print(b)
# operation_according_data_type()

# Sort a list without using the sort function (I could'n do it, so i took help of our teacher :( )
def sorting():
    a = [3,4,5,6,7,8,1,7,2,8]
    for i in range(len(a)):
        for j in range(0,len(a)-i-1):
            if a[j] < a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]
    print(a)
# sorting()
# Find out the second smallest element of a list
def second_smallest_element():
    a = [3,4,5,6,7,8,1,7,2,8]
    for i in range(len(a)):
        for j in range(0,len(a)-i-1):
            if a[j] < a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]
    print(a[-2])
# second_smallest_element()

