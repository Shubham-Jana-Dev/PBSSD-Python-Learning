# 🗓️ Day 29: Dictionaries, Sets, and Tuples

**Topic:** Mapping Data, Unique Collections, and Immutable Sequences.

---

## 🛠️ Concepts Covered

### 1. Dictionaries (Key-Value Pairs)
I explored how to store data in a non-linear way using unique keys.
* **CRUD Operations:** Practiced adding new keys (`Status`), updating existing values (`current year`), and removing elements using `.pop()`.
* **Nested Dictionaries:** Built a `student_status` tracker where each student name maps to another dictionary of results—a common structure for JSON APIs.
* **Retrieval Logic:** Used `.get()` and `.keys()` to safely access data without causing KeyErrors.



### 2. Set Theory & Operations
I moved beyond lists to **Sets**, which are unordered collections of unique elements.
* **Mathematical Operations:** Mastered Union (`|`), Intersection (`&`), Difference (`-`), and Symmetric Difference (`^`).
* **Subsets & Supersets:** Used `.issubset()` and `.issuperset()` to compare collections.
* **Safe Removal:** Learned the difference between `.remove()` (raises error if missing) and `.discard()` (fails silently).



[Image of Venn diagram showing set union, intersection, and difference]


### 3. Tuples (Immutable Sequences)
* **Immutability:** Recognized that tuples cannot be changed after creation, making them safer for data that should remain constant.
* **Sorting:** Learned that while tuples are immutable, we can use `sorted(my_tuple)` to return a *new* sorted list or tuple.

---

## 📝 Practical Implementation Summary

| Structure | Key Feature | Operations Performed |
| :--- | :--- | :--- |
| **Dictionary** | Associative Mapping | Updated Attendance, Status Check, Student Pass/Fail count. |
| **Set** | Uniqueness | Union, Intersection, Disjoint checks, Add/Update/Discard. |
| **Tuple** | Fixed Data | Element counting, Membership checking (`in`), Reverse sorting. |

---

## 💡 Engineering Insight: Choosing the Structure
Today's lab taught me that data structure choice depends on the goal:
* Use a **Dictionary** when you need to look up a value by a specific name (ID, Username).
* Use a **Set** when you want to remove duplicates or perform mathematical comparisons.
* Use a **Tuple** when you want to ensure the data cannot be accidentally modified by another part of the program.

---

## 🚀 Repository Link
💻 **GitHub Repo:** [PBSSD-Python-Learning](https://github.com/Shubham-Jana-Dev/PBSSD-Python-Learning)
