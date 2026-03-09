import time
import sys

def profile_data_structure(data, name, target):
    size_in_mb = sys.getsizeof(data)/(1024**2)

    start = time.time()
    _ = target in data
    end = time.time()
    duration = end - start

    return{"name":name, 'size':size_in_mb, 'time':duration}

limit = 10000000
target = 9999999

raw_list = list(range(limit))
results = [profile_data_structure(raw_list, "List", target),profile_data_structure(set(raw_list), "Set", target),profile_data_structure({k: k for k in raw_list}, "Dictionary", target)]

baseline = results[0]
for i in range(1, len(results)):
    current = results[i]
    time_saved = baseline['time'] - current['time']
    mem_cost = current['size'] - baseline['size']
    
    print(f"--- {current["name"]} vs {baseline['name']} ---")
    print(f"Time saved: {time_saved:.6f}s")
    print(f'RAM Cost: {mem_cost:.2f} MB')

    if mem_cost > 0:
        score = (time_saved*1e9)/(mem_cost * 1024)
        print(f"Efficiency Score: {score:.2f} ns/KB")

print(f"List Size: {sys.getsizeof(list(range(10000000)))} bytes")
print(f"Generator Size: {sys.getsizeof(range(10000000))} bytes")