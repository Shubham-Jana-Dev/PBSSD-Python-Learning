# --- Armstrong Number Logic ---

num = int(input("Enter the number: "))
temp1 = num
temp2 = num 
length = len(str(num)) # Efficient way to get length
total_sum = 0

# Calculating Armstrong Sum
while temp2 != 0:
    rem = temp2 % 10
    total_sum += (rem ** length)
    temp2 //= 10

if total_sum == num: # Fixed: use == for comparison
    print(f"{num} is an Armstrong number")
else:
    print(f"{num} is NOT an Armstrong number")
    
# --- Range & For Loop Experiments ---

print("\n--- Range Experiments ---")
# m = starting value, n = ending value
for i in range(1, 5): 
    print(i) # Prints 1, 2, 3, 4

# Reverse Step

for i in range(5, 1, -1):
    print(f"Counting down: {i}")

# Boolean/Zero ranges (These won't print anything as range is empty)
for I in range(False): # range(0)
    print("This won't show")

# Summing a range
x, y = 10, 20
total = 0
for i in range(x, y):
    total += i
print(f"Sum of range {x} to {y} is: {total}")
