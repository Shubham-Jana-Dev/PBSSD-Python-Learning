# --- Armstrong Number Logic ---
"""
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
"""
# --- Range & For Loop Experiments ---
print("\n--- Range Experiments ---")
# m = starting value, n = ending value
for i in range(1, 5): 
    print(i) # Prints 1, 2, 3, 4