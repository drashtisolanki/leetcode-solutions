# Arrays
This folder contains LeetCode array problems.

# 📘 LeetCode Arrays Solutions

This folder contains solutions to array problems from LeetCode.

---

## 🔢 Problem 1: Remove Duplicates from Sorted Array (LeetCode 26)

### 🧠 Approach

#### 🔹 Brute Force Approach
- Use nested loops to compare each element with others  
- Remove duplicates manually  

📌 **Time Complexity:** O(n²)  
📌 **Space Complexity:** O(1)  

---

#### 🔹 Optimal Approach (Two Pointer Technique)
- Use two pointers:
  - `i` → tracks the last unique element  
  - `j` → iterates through the array  

- Compare `nums[j]` with `nums[i]`  
- If different:
  ```python
  i += 1
  nums[i] = nums[j]

📌 **Time Complexity:** O(n)  
📌 **Space Complexity:** O(1)  
