# 🗓️ Day 20: Error Handling & Dynamic Arguments

**Topic:** Exception Handling (Try-Except) and advanced function flexibility (*args, **kwargs).

---

## 🛠️ Concepts Covered

### 1. Robustness with Try-Except
* **NameError:** Handled cases where variables are referenced before assignment or defined incorrectly.
* **ValueError:** Implemented recursive error handling to catch invalid data types during `input()` (e.g., entering a string when an integer is expected).



### 2. Flexible Argument Handling
* **`*args` (Non-keyword arguments):** Mastered unpacking tuples to allow a customer to order "any number" of extra toppings or items.
* **`**kwargs` (Keyword arguments):** Used dictionary-style arguments to pass specific pairs, like `item=price` or `detail=value`.
* **Unpacking Operators:** Practiced using `*` and `**` to pass existing tuples and dictionaries into functions.

### 3. The "Smart Billing" Challenge
Developed a logic that cross-references a list of items (`*args`) against a price database (`**kwargs`). 
* **Key Logic:** `if item in kwargs:` to dynamically calculate totals while flagging missing price data.

---

## 📝 Practical Implementations
* **`ValueErrorHandling`**: A self-healing input function.
* **`understanding_both_at_once`**: A master function handling positional, variable, and keyword arguments simultaneously.
* **`smart_bill1`**: A real-world application of data matching and summation.

---

## 💡 Engineering Insight: Fault Tolerance
In software engineering, we assume the user **will** make a mistake. By using `try-except`, we ensure the program remains operational. Combining this with `*args` allows us to build APIs that don't break when the amount of incoming data changes.