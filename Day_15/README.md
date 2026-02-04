# 🗓️ Day 15: Geometric Logic & Advanced Pattern Design

**Topic:** Multi-conditional logic and coordinate-based region filling.

---

## 🛠️ Pattern Engineering
Today focused on combining multiple diagonal and boundary conditions to create complex character shapes:
* **The "N" Shape:** `j == 1 or j == Rg or j == i`
* **The "Z" Shape:** `i == 1 or i == Rg or i + j == Rg + 1`
* **The "Hourglass":** Combining top/bottom boundaries with intersecting diagonals.

### 💡 B.Tech Insights
1. **Shadow Effect:** Using inequalities like `j >= i` allows for filling whole sections to create solid triangles.
2. **Symmetry:** Learned that `(f + 1) // 2` is the ideal midpoint for odd-numbered ranges.

---

## 📝 Files
* **day15_pbssd_pattern_printing.py**: Implementation of N, Z, and complex boxed patterns.