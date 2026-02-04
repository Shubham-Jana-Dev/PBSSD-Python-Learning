# 🗓️ Day 12: Armstrong Numbers & For-Loop Iterators

**Topic:** Digit manipulation, Indexing, and the `range()` function.

---

## 🛠️ Key Concepts

### 1. Armstrong Number Logic
A number is an **Armstrong number** if the sum of its own digits, each raised to the power of the number of digits, equals the number itself.
* **Example ($n=3$):** $153 \rightarrow 1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153$.

### 2. The `for` Loop
* **Stream Processing:** Used when the number of executions is known in advance.
* **Zero-based Indexing:** Python treats sequences (strings, lists) as data streams starting at **index 0**.

### 3. The `range()` Function
* **`range(n)`**: Starts at 0, ends at $n-1$.
* **`range(m, n)`**: Starts at $m$, ends at $n-1$.
* **`range(m, n, -1)`**: Used for reverse iteration.

---

## 📝 Practical Implementations
* **day12_pbssd.py**: Contains the logic for Armstrong number detection and range-based iterators.

---

## 🚀 Sneak Peek
Today introduced the concept of **Reusability** using the `def` keyword and the `return` statement to pass values back from logic blocks.