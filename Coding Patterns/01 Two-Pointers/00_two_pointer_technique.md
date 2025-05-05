
# 🧠 Two-Pointer Technique in Python

## 📌 What is the Two-Pointer Technique?

The **Two-Pointer Technique** is an efficient algorithmic approach that uses **two variables (pointers)** to iterate through a data structure like a list, array, or string.

Depending on the problem, the two pointers can move:
- From both ends toward the center
- From the start, with different speeds
- Overlapping to maintain a "window"

---

## 🎯 Purpose

The goal of using two pointers is to solve problems **faster**, often reducing the time complexity from `O(n²)` (brute force) to `O(n)`.

---

## 🧠 When to Use It?

You should consider using the **Two-Pointer Technique** when:

- You are working with **sorted arrays or strings**
- You need to **find a pair or subarray** that satisfies a condition (e.g., sum, length, value)
- You want to **shrink or expand a window** (sliding window problems)
- You want to **traverse from both ends** of a list (e.g., palindrome problems)

---

## 🔍 How to Identify If Two Pointers Can Be Used

Ask yourself:
- Is the array **sorted** or can it be sorted?
- Am I checking **pairs**, **windows**, or **boundaries**?
- Am I required to **optimize** beyond brute force?
- Is the **comparison** between elements in different parts of the array?

If yes to most of these — Two Pointers may be the way to go.

---

## 🧩 What Kind of Problems Can It Solve?

| Problem Type | Description |
|--------------|-------------|
| **Pair Sum** | Find if a pair of elements adds up to a target sum |
| **Palindrome Check** | Compare characters from both ends |
| **Reverse Operations** | Reversing arrays or strings |
| **Remove Duplicates** | Especially in sorted arrays |
| **Sorted Merging** | Merging two sorted arrays/lists |
| **Subarray Sliding Window** | Minimum or maximum length subarray problems |

---

## 🧪 Example 1: Find if Pair Exists with Target Sum

```python
def has_pair_with_sum(arr, target):
    arr.sort()
    left, right = 0, len(arr) - 1

    while left < right:
        current_sum = arr[left] + arr[right]
        if current_sum == target:
            return True
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    return False
```

---

## 🧪 Example 2: Check if a String is Palindrome

```python
def is_palindrome(s):
    left, right = 0, len(s) - 1

    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True
```

---

## 🧪 Example 3: Remove Duplicates from Sorted Array (Leetcode 26)

```python
def remove_duplicates(nums):
    if not nums:
        return 0

    slow = 0
    for fast in range(1, len(nums)):
        if nums[slow] != nums[fast]:
            slow += 1
            nums[slow] = nums[fast]

    return slow + 1
```

---

## 📌 Summary

| Concept | Details |
|--------|---------|
| Technique | Use two pointers to traverse a list efficiently |
| Purpose | Optimize time complexity (usually `O(n)`) |
| When to Use | Sorted data, finding pairs, checking windows/boundaries |
| Identifiable Clues | Pair problems, palindromes, subarrays, sorted inputs |
| Common Problems | Pair sum, palindrome, duplicates, merge, sliding window |

---

## 💡 Tip:

In interviews, always ask:
- "Can I sort the input?"
- "Can I use two indices to avoid nested loops?"

If yes, this technique might be a perfect fit.
