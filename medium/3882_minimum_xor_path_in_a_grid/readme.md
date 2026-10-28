# 3882. Minimum XOR Sum of Path in Grid

## Problem

Given an `m x n` grid of integers, find the **minimum XOR sum** of any valid path from the top-left cell `(0, 0)` to the bottom-right cell `(m-1, n-1)`.

A valid path consists of moves only **right** or **down**. The XOR sum of a path is the XOR of all values on the cells visited along the path (including both endpoints).

---

## Approach: Dynamic Programming with XOR Set Propagation

### Intuition

Each cell `(i, j)` can be reached from `(i-1, j)` (above) or `(i, j-1)` (left). For every reachable XOR value at those predecessor cells, we can extend the path to `(i, j)` by XOR-ing with `grid[i][j]`.

Since `grid[i][j] <= 1000`, the XOR of any path is at most `1023` (10 bits). Thus each cell stores at most 1024 distinct values — a small constant.

### Algorithm

1. `dp[i][j]` is a **set** of all possible XOR sums reachable at cell `(i, j)`.
2. Initialize `dp[0][0] = {grid[0][0]}`.
3. Fill the first column: each cell inherits from the cell above.
4. Fill the first row: each cell inherits from the cell to the left.
5. For each remaining cell `(i, j)`:
   - Take all XOR values from `dp[i-1][j]` (above), XOR each with `grid[i][j]`, add to `dp[i][j]`.
   - Take all XOR values from `dp[i][j-1]` (left), XOR each with `grid[i][j]`, add to `dp[i][j]`.
6. The answer is `min(dp[m-1][n-1])`.

### Why This Works

- Every valid path from `(0,0)` to `(i,j)` corresponds to exactly one sequence of right/down moves. By processing cells in row-major order, all such paths are enumerated.
- Using a `set` automatically deduplicates identical XOR values, keeping memory bounded.
- The XOR value range is capped at `1023`, so each `set` holds at most 1024 elements regardless of path count.

### Edge Cases

- Single cell (`m=1, n=1`): answer is `grid[0][0]`.
- Single row or single column: only one path exists, XOR sum is deterministic.

---

## Complexity

- **Time**: O(m × n × 1024) — for each cell, iterate over at most 1024 values from predecessor sets.
- **Space**: O(m × n × 1024) — each cell stores a set of at most 1024 integers. In practice this fits within memory limits.