
# 0062. Unique Paths

## Problem

There is an `m x n` grid. A robot is located at the top-left corner `(0, 0)` and wants to reach the bottom-right corner `(m-1, n-1)`. The robot can only move **right** or **down** at any point in time. Return the number of unique paths to the destination.

---

## Approach: Dynamic Programming

### Intuition

To reach any cell `(i, j)`, the robot must come from either:
- The cell above `(i-1, j)` (by moving down)
- The cell to the left `(i, j-1)` (by moving right)

Therefore, the number of ways to reach `(i, j)` is the sum of ways to reach those two predecessor cells:

```
dp[i][j] = dp[i-1][j] + dp[i][j-1]
```

### Base Cases

- Cells in the first row `(0, j)`: only reachable by moving right from `(0,0)` → exactly **1** way.
- Cells in the first column `(i, 0)`: only reachable by moving down from `(0,0)` → exactly **1** way.

### O(mn) Space DP — Full 2D Table

Construct a 2D `dp` table initialized with base cases. Fill it row by row using the recurrence above. The answer is `dp[m-1][n-1]`.

- **Time**: O(m × n) — every cell computed once.
- **Space**: O(m × n) — storing the full 2D table.

---

### O(n) Space DP — Rolling Array

Since `dp[i][j]` only depends on the current row (`dp[i][j-1]`) and the previous row (`dp[i-1][j]`), we can compress the table into a single 1D array of length `n`.

The array `dp[j]` represents the current row's values. For each new row `i`:
- `dp[0]` stays `1` (first column base case).
- For `j ≥ 1`: `dp[j] = dp[j-1] + dp[j]`, where `dp[j-1]` is the updated left value and `dp[j]` (before overwrite) is the value from the previous row above.

- **Time**: O(m × n) — same number of computations.
- **Space**: O(n) — only one row stored.

---

### Walkthrough (O(n) Space)

`m = 3, n = 7`

Initial `dp = [1, 1, 1, 1, 1, 1, 1]`

| row i | dp before         | dp after update       |
|-------|-------------------|-----------------------|
| 1     | `[1,1,1,1,1,1,1]` | `[1,2,3,4,5,6,7]`     |
| 2     | `[1,2,3,4,5,6,7]` | `[1,3,6,10,15,21,28]` |

Result: **28** unique paths.

This matches the combinatorial formula: $\binom{m+n-2}{m-1} = \binom{8}{2} = 28$.

---

### Edge Cases

- `m = 1` or `n = 1`: only one straight path → returns `1`.
- Both `m = 1, n = 1`: already at destination → returns `1`.

---

## Complexity Summary

| Method        | Time     | Space    |
|---------------|----------|----------|
| 2D DP         | O(m × n) | O(m × n) |
| 1D Rolling DP | O(m × n) | O(n)     |

---

## Key Takeaway

> Grid path-counting problems follow a universal DP pattern: **`dp[i][j] = dp[i-1][j] + dp[i][j-1]`**. Whenever you see "only move right/down" or "only move in two directions," think DP with base cases on the boundary. Space can almost always be compressed to O(min(m, n)) by rolling the array — a useful optimization to recognize.
