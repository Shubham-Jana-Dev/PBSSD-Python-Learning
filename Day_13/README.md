# 🗓️ Day 13: Nested Loops & Pattern Geometry

**Topic:** Coordinate-based iteration and the "Clock Hand" model.

---

## 🛠️ Logic & Theory

### 1. The "Clock Hand" Model
* **Outer Loop:** Acts like the hour hand; it moves once only after the inner loop completes a full cycle.
* **Inner Loop:** Acts like the minute hand; it completes all its iterations for every single step of the outer loop.

### 2. Geometric Mapping
By treating loop variables `i` (rows) and `j` (columns) as coordinates, I implemented several patterns:
* **Left Triangle:** `if i >= j`
* **Right Triangle:** `if i + j >= r + 1`
* **Diagonal (X-Shape):** `if i == j or i + j == r + 1`
* **Hollow Square:** `if i == 1 or j == 1 or i == r or j == r`

---

## 📝 Practical Implementations
* **day13_pbssd.py**: Core logic for nested loop theory.
* **day13_pbssd_pattern_printing.py**: Geometric star patterns using coordinate logic.