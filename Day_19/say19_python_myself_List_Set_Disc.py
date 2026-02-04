def print_A_disc(my_dic):
    print(my_dic) 
my_Dictionary = {1,2,3,4,5,2,7,9,90}
# print_A_disc(my_Dictionary)
'''
{1, 2, 3, 4, 5, 7, 9, 90}   ---> Output
the out put will return the with only all the unique elemets of the dictionary. Because a dictionary 
does not store same alement multiple times.
'''

# create a new list of all unique elements from the given list My_list = [1,32,4,65,4,3,2,1,6,65,7,8,7,9,90,32,4,2,1,6]
def Create_unique_list(list1):
    temp = set(list1)
    new_list = list(temp)
    return new_list
My_list = [1,32,4,65,4,3,2,1,6,65,7,8,7,9,90,32,4,2,1,6]
result = Create_unique_list(My_list)
# print(result)


def understanding_the_indexing_featureIn_list_and_tupple(My_list1,listIndex,My_tupple,tuppleIndex):
    print(My_list1[listIndex])
    print(My_tupple[tuppleIndex])
A_list = [32, 1, 65, 3, 342, 2, 6, 7, 8, 9, 90]
A_tupple = (32, 1, 65, 3, 342, 2, 6, 7, 8, 9, 90)
# understanding_the_indexing_featureIn_list_and_tupple(A_list,4,A_tupple,4)


'''                      ---------List VS Set---------
The main difference between lists and tupples is, lists are mutable means we can upadet it's data elements
or we can add elements (.append) or remove elements (.remove).
but we cant any operation in the tupple so sets are immutable.
'''
def exploring_append_in_list(the_lis,new_e):
    the_lis.append(new_e)
    return the_lis
the_list = [1,2,3,4,5,6]
New_element = 7
result01 = exploring_append_in_list(the_list,New_element)
# print(result01)


def exploring_remove_in_list(the_lis,new_e):
    the_lis.remove(new_e)
    return the_lis
the_list02 = [10,62,43,5,54,5,60]
Old_element = 5
result02 = exploring_remove_in_list(the_list02,Old_element)
# print(result02)


def exploring_add_in_set(the_set01,new_element01):
    the_set01.add(new_element01)
    return the_set01
the_list02 = {1,2,3,4,5,6,7}
New_element = 8
result022 = exploring_add_in_set(the_list02,New_element)
print(result022)


def exploring_remove_in_set(the_set02,old_element02):
    the_set02.remove(old_element02)
    return the_set02
the_list02 = {1,2,3,4,5,6,7}
Old_element = 6
result022 = exploring_remove_in_set(the_list02,Old_element)
print(result022)


def update_index_from_list(y_list,index_num,new_element99):
    y_list[index_num] = new_element99
    return y_list
lis = [44,3,21,1,2,3,434,2,6,4]
update_requireAt = 6
new_number_should_be = 55
result99 = update_index_from_list(lis,update_requireAt,new_number_should_be)
print(result99)


def update_index_from_set(y_set,index_num,new_element991):
    y_set.remove(index_num)
    y_set.add(new_element991)
    return y_set
set1 = {44,3,21,1,22,443,434,2,6,4}
unwanted = 3
new_number_should_be = 55
result991 = update_index_from_set(set1,unwanted,new_number_should_be)
print(result991)