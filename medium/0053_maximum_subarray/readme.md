# 0053. Maximum Subarray

## Problem

Given an integer array `nums`, find the contiguous subarray (containing at least one number) that has the **largest sum**, and return its sum.

---

## Approach

### O(n³) Brute Force — Enumerate All Subarrays

Triple nested loop: outer two loops enumerate every `(start, end)` pair, and the innermost loop computes the sum of that subarray. Track the maximum sum seen.

- **Time**: O(n³) — for each of O(n²) subarrays, summing takes O(n).
- **Space**: O(1).

This is the most naive approach and will TLE on large inputs, but it establishes correctness by checking every possibility exhaustively.

---

### O(n²) Brute Force — Running Sum

Eliminate the innermost loop by accumulating the sum as the `end` pointer expands:


for start in range(n):
    current_sum = 0
    for end in range(start, n):
        current_sum += nums[end]
        ans = max(ans, current_sum)


- **Time**: O(n²) — each subarray sum is computed in O(1) incremental time.
- **Space**: O(1).

Still too slow for n ≤ 10⁵, but a meaningful improvement over O(n³).

---

### O(n) Space DP — Kadane's Algorithm (Explicit DP Array)

**Key insight**: For each position `i`, the maximum subarray ending at `i` is either:
- Extend the best subarray ending at `i-1` by including `nums[i]`
- Start fresh from `nums[i]` itself

Formally: `dp[i] = max(dp[i-1] + nums[i], nums[i])`

The answer is `max(dp)` over all `i`.

- **Time**: O(n) — single pass.
- **Space**: O(n) — storing the full `dp` array.

This is the first efficient solution. It captures the essential greedy choice: **never carry a negative prefix forward**.

---

### O(1) Space DP — Kadane's Algorithm (Rolling Variable)

Since `dp[i]` only depends on `dp[i-1]`, we can replace the array with a single variable `current` representing the maximum sum ending at the current index.


current = max(current + nums[i], nums[i])
ans = max(ans, current)


- **Time**: O(n) — single pass.
- **Space**: O(1) — only two integer variables.

This is the canonical optimal solution. It is both the fastest and most memory-efficient approach.

---

## Walkthrough (O(1) DP)

`nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]`

| i | nums[i] | current = max(current+nums[i], nums[i]) | ans |
|---|---------|----------------------------------------|-----|
| 0 | -2 | -2 | -2 |
| 1 | 1 | max(-2+1, 1) = 1 | 1 |
| 2 | -3 | max(1-3, -3) = -2 | 1 |
| 3 | 4 | max(-2+4, 4) = 4 | 4 |
| 4 | -1 | max(4-1, -1) = 3 | 4 |
| 5 | 2 | max(3+2, 2) = 5 | 5 |
| 6 | 1 | max(5+1, 1) = 6 | 6 |
| 7 | -5 | max(6-5, -5) = 1 | 6 |
| 8 | 4 | max(1+4, 4) = 5 | 6 |

Result: **6** (subarray `[4, -1, 2, 1]`).

---

## Edge Cases

- All negative numbers: e.g., `[-3, -1, -2]` → returns `-1` (the single largest element, since at least one element must be chosen).
- Single element: returns that element.
- All positive: returns `sum(nums)`.

---

## Complexity Summary

| Method | Time | Space |
|--------|------|-------|
| O(n³) brute force | O(n³) | O(1) |
| O(n²) running sum | O(n²) | O(1) |
| DP (explicit array) | O(n) | O(n) |
| DP (rolling variable) | O(n) | O(1) |

---

## Key Takeaway

> Kadane's algorithm is the canonical solution to maximum subarray problems. The core principle — **"extend the current run if it helps, otherwise restart"** — applies broadly to any optimization problem where local decisions determine global optima (e.g., maximum product subarray, maximum circular subarray).