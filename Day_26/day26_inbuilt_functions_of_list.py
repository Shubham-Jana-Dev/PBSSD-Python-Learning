# 1. write a program to find the length of a list
# Using loop
def len_calculation_using_loop():
    My_list = [12,13,14,17,51,33]
    count = 0
    for i in My_list:
        count += 1
    print(count)
# len_calculation_using_loop()

# Using inbuilt function
def using_inbuilt_func():
    My_list = [22,43,5,76,33,'Shubham',2036]
    print(len(My_list))
# using_inbuilt_func()

# 2. How could you access first and the last element of a list.
def access_first_and_last():
    My_list = ['public Bus',1,1.1,1.2,'.....',99.8,99.9,100,'BMW']
    print(f"The first element = {My_list[0]}\nThe last element = {My_list[len(My_list)-1]}")
# access_first_and_last()

# 3. Write a program to add a element at the end of a list.
def element_add_at_last():
    My_list = ['laptop','the potential','phone','classes']
    My_list.append('The Why')
    print(My_list)
# element_add_at_last()

# 4. Write a element to insert a new element in a specific position inside a list.
def element_insert():
    My_list = ['fingers','vision','vs code','70 wpm']
    My_list.insert(2,'hunger of exploration')
    print(My_list)
# element_insert()

# 5. Write a program to remove an element from a list.
def remove_form_list():
    My_list = ['PBSSD','python','late night coding','sleep']
    My_list.remove('sleep')
    print(My_list)
# remove_form_list()

# 6. Write a program to find out the maxium element.
# Using the loop
def maximum_element():
    t=0
    marks = [89,90,96,99,87,100,95]
    for i in marks:
        if t<i:
            t = i
    print(t)
# maximum_element()
def max_func():
    marks = [89,90,96,99,87,100,95]
    print(max(marks))
# max_func()

# 7. Write a program to count how many times an element appears in the list?
def using_count_func():
    my_list = [1,2,3,2,4,5,2,6,5,2,10]
    print(my_list.count(2)) 
using_count_func()       