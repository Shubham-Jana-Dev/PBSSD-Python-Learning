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