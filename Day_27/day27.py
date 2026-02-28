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
by_list_comprehension()
