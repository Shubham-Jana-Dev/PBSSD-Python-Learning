# 🗓️ Day 19: Advanced Data Structures Lab

**Topic:** Deep dive into Mutability, Uniqueness, and Storage Logic (List vs. Tuple vs. Set).

---

## 🛠️ Concepts Covered

### 1. The Set Uniqueness Principle
* **Automatic De-duplication:** Learned that a `set` is a collection of unique elements. Passing a list with duplicates through a set is the most efficient way to clean data.
* **Storage Logic:** Unlike lists, sets are **unordered**. You cannot rely on index positions.

### 2. Mutability Comparison
I explored how Python handles memory for different "containers":

| Data Structure | Ordered | Mutable | Symbol | Method to Add |
| :--- | :--- | :--- | :--- | :--- |
| **List** | Yes | Yes | `[]` | `.append()` |
| **Tuple** | Yes | **No** | `()` | N/A (Read-only) |
| **Set** | No | Yes | `{}` | `.add()` |



### 3. Positional vs. Value-Based Updating
* **Positional (Lists):** Accessed via index (e.g., `list[4] = 99`).
* **Value-Based (Sets):** Since sets lack indexes, "updating" requires removing the old value and adding the new one.

---

## 📝 Practical Implementations in `day19_pbssd.py`

* **`create_unique_list(list1)`**: Efficiently cleans a list by casting to a set and back to a list.
* **`check_indexing`**: A comparative function demonstrating that Tuples support read-access by index, even though they are immutable.
* **`update_set_value`**: A custom workaround to "edit" data within an unordered set collection.

---

## 💡 Engineering Insight: Memory & Performance
In a B.Tech context, understanding these structures is about **Time Complexity**. 
- Searching for an element in a **List** takes **O(n)** time (checking every item). 
- Searching in a **Set** takes **O(1)** time due to **Hashing**, making it the superior choice for large-scale data lookups.