<p align="center">
  <img src="assets/PBSSD.png" alt="PBSSD Logo" width="200">
</p>

# 🐍 PBSSD Python Programming Journey

Welcome to my learning repository! This project documents my progress in the **Paschim Banga Society for Skill Development (PBSSD)** Python Programming course. Here, I store my daily notes, practice scripts, and logic-building exercises.

---

## 🗓️ Day 01: The Foundations of Python
**Date:** December 18, 2025  
**Focus:** Development Environments, Dynamic Typing, and Memory Management.

### 1. Understanding the Environment
* **IDLE:** Explored the Interactive Shell for quick testing and Script Mode for permanent programs.
* **PVM (Python Virtual Machine):** Learned how the internal engine executes our source code.

### 2. Key Technical Concepts
* **Dynamic Typing:** Verified classes (`int`, `str`, `float`, `list`) using the `type()` function.
* **Memory Management:** Used `id()` to fetch unique memory addresses of objects.
* **Keywords:** Utilized the `keyword` module to identify reserved words.

---

## 🗓️ Day 02: Identifiers, Variables, and Memory
**Date:** December 19, 2025  
**Focus:** Naming conventions, ASCII values, and memory optimization.

### 1. Python Identifiers
* **Case Sensitivity:** Learned how Python differentiates names based on **ASCII** values.
* **Naming Rules:** Mastered rules for valid identifiers (no leading digits, no special symbols except `_`).
* **Built-in Functions:** Used `ord()` for character-to-ASCII and `chr()` for ASCII-to-character conversion.

---

## 🗓️ Day 03: Variable Scope & Memory Stack
**Date:** December 20, 2025  
**Focus:** Local vs. Global variables and LIFO memory logic.

### 1. Scope and Accessibility
* **Local Variables:** Declared inside blocks/functions; restricted visibility to that local area.
* **Global Variables:** Declared at the top level; accessible throughout the script.
* **The `global` Keyword:** Learned to modify global values from within a local scope.

### 2. Memory Logic (LIFO)
* **Stack Memory:** Explored how Python manages function calls using the **Last-In, First-Out** principle.

### 3. Homework & Problem Solving
* **Solved 12 logic-based questions** regarding variable scope and memory output.
* Solutions are available in the [Day_03 Folder](./Day_03).
---

## 🚀 Day 03: Practical Assignment Showcase
**Total Tasks:** 12 Python Scripts  
**Objective:** Mastering arithmetic operators, user input handling, and mathematical logic using "Pure Python" (No external modules).

### 🛠️ Problem-Solving Highlights
Below is the list of 12 logic-based programs I developed and pushed to the `Day_03/` folder:

| No. | Problem Statement | Core Logic / Formula |
| :--- | :--- | :--- |
| 01 | **Area of Parallelogram** | `base * height` |
| 02 | **Area of Conical Vessel** | $A = \pi r (l + r)$ (using $l = \sqrt{r^2 + h^2}$) |
| 03 | **Area of Parallelepiped** | $2 \times (ab + bh + ha)$ |
| 04 | **Quadratic Equation** | Used discriminant $d = b^2 - 4ac$ and roots formula |
| 05 | **Equilateral Triangle** | $Area = \frac{h^2}{\sqrt{3}}$ |
| 06 | **Area of Ellipse** | $\pi \times a \times b$ |
| 07 | **KM to Miles** | $km \times 0.6214$ |
| 08 | **Right-Angle Check** | Pythagorean Theorem: $a^2 + b^2 == c^2$ (Boolean logic) |
| 09 | **Temp Converter** | $C \rightarrow F$ and $C \rightarrow K$ |
| 10 | **Rhombus & Half-Circle** | $\frac{d_1 \times d_2}{4}$ and $\frac{\pi r^2}{2}$ |
| 11 | **Surface Area of Cube** | $6 \times s^2$ |
| 12 | **Precision Heron's** | Unit conversion: $cm \rightarrow m$ and $\mu m \rightarrow m$ |

### 🔍 Technical Observation
During this assignment, I practiced **Precision Unit Conversion**. In Task 12, I manually converted $2.3 \text{ cm}$ and $6.31 \text{ }\mu\text{m}$ to meters to ensure the dimensions were standardized before applying Heron's Formula.



---
---

## 🗓️ Day 04: Literals & Number Systems
**Date:** December 21, 2025  
**Focus:** Data types (Literals) and Base-N number representations.

### 1. Python Literals
Literals are constant values assigned to variables. I practiced identifying various types:
* **Numeric:** `int` (19), `float` (45.7), `complex` (10+20j).
* **Boolean:** `True` / `False`.
* **Collections:** `list` [ ], `tuple` ( ), `set` { }, and `dict` {key:value}.

### 2. Integral Representations (Number Systems)
Python allows representing integers in four different bases:

| System | Base (Radix) | Prefix | Digits |
| :--- | :--- | :--- | :--- |
| **Decimal** | 10 | None | 0-9 |
| **Binary** | 2 | `0b` or `0B` | 0, 1 |
| **Octal** | 8 | `0o` or `0O` | 0-7 |
| **Hexadecimal**| 16 | `0x` or `0X` | 0-9, A-F |

### 3. Conversion Functions
* **`bin()`**: Converts an integer to its binary string representation.
* **`oct()`**: Converts an integer to its octal string representation.
* **`hex()`**: Converts an integer to its hexadecimal string representation.

## 📂 Repository Structure
```text
PBSSD-PYTHON-LEARNING/
├── assets/
│   └── PBSSD.png
├── Day_01/
│   └── day01_pbssd.py
├── Day_02/
│   └── day02_pbssd.py
├── Day_03/
│   ├── Assignment_day03.py
│   └── day03_pbssd.py
├── .gitignore
├── LICENSE
└── README.md
