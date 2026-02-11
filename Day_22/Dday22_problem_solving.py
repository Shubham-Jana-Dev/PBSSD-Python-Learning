"""
The Final "Master Chef" Challenge 🏆
You are ready for the final boss of this logic series. Let's do the Price Calculation challenge I mentioned.

The Goal: Write calculate_bill(tax_rate, *args, **kwargs)
Ingredients (*args): Each costs $2.
Extras (**kwargs): The value is the price (e.g., avocado=1.5).
The Logic:
Sum up the total.
Discount: If the total is over $20, subtract $5.
Tax: Apply the tax_rate to the final amount.
Print the Grand Total.
Example: calculate_bill(0.10, "Bread", "Ham", "Cheese", avocado=2.0) 

Calculation: ($2+2+2) + 2.0 = 8.0. Total: 8.0+10% tax=8.8
"""
def calculate_bill(tax_rate,*args,**kwargs):
    total =  0
    for i in args:
        total += 2
    for i in kwargs:
        total += kwargs[i]
    if total > 20:
        total -= 5
    final_bill = total + total*tax_rate
    return final_bill
calculate_bill(0.08, coffee=3.00, cookie=2.00)