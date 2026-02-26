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