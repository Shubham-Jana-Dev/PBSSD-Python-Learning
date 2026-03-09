import time
print(time.asctime())
large_list = list(range(10000000))
large_set = set(large_list)
my_dict = {key: key**2 for key in large_list}
target = 9999999

def run_benchmark(data_structure,name):
    start_time = time.time()
    _ = target in data_structure
    end_time = time.time()
    total_consumed_time = end_time - start_time
    print(f"The searching time for {name} is {total_consumed_time:.6f}.")

run_benchmark(large_list,"List")
run_benchmark(large_set,"Set")
run_benchmark(my_dict,"Dictionary")

#2026-03-10
import sys
list_size = sys.getsizeof(large_list)
set_size = sys.getsizeof(large_set)
dict_size = sys.getsizeof(my_dict)

print(list_size)
print(set_size)
print(dict_size)

def size_compare(size_of_data_structure1,size_of_data_structure2,name1,name2):
    if size_of_data_structure1 > size_of_data_structure2:
        print(f'the {name1} is {size_of_data_structure1 - size_of_data_structure2} unit larger than the {name2}.')
    else:
        print(f'the {name2} is {size_of_data_structure2 - size_of_data_structure1} unit larger than the {name1}')

size_compare(list_size,set_size,'List','Set')
size_compare(set_size,dict_size,'Set','Dictionary')
size_compare(list_size,dict_size,'List','Dictionary')