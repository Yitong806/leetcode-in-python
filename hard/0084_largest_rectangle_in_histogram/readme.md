# 84. Largest Rectangle in Histogram

## Problem

Given an array of integers `heights` representing the heights of bars in a histogram (each bar has width 1), return the area of the largest rectangle that can be formed within the histogram.

---

## Approach 1: Brute Force — Expand Left and Right

For each bar at index `i`, find how far it can extend to the left and right while remaining the shortest bar in that range.

### Algorithm

1. For each bar `i` from `0` to `n-1`:
   - **Scan left**: move from `i-1` down to `0`, stop at the first bar shorter than `heights[i]`. All bars visited are part of the rectangle.
   - **Scan right**: move from `i+1` up to `n-1`, stop at the first bar shorter than `heights[i]`. All bars visited are part of the rectangle.
   - **Width** = `right - left + 1` (both boundaries inclusive).
   - **Area** = `heights[i] * width`.
2. Track the maximum area across all bars.

### Why This Works

Each bar is treated as the minimum height of a candidate rectangle. By expanding left and right until a shorter bar is found, we guarantee the widest possible rectangle where `heights[i]` is the limiting height.

### Complexity

- **Time**: O(n²) — for each of the n bars, we may scan up to O(n) elements left and right.
- **Space**: O(1) — only variables for tracking boundaries and maximum.

### Limitation

This approach times out on large inputs (n up to 10⁵). It serves as a correctness baseline and a stepping stone to the optimal solution.

---

## Approach 2: Monotonic Increasing Stack (Optimal)

### Intuition

Instead of scanning left and right for every bar, we maintain a stack that caches boundary information incrementally. When a bar is "blocked" by a shorter bar on its right, we compute its maximum rectangle immediately.

### Algorithm

1. Append a sentinel `0` to `heights` to force all remaining bars to be evaluated at the end.
2. Traverse `i` from `0` to `n` (including sentinel):
   - While stack is not empty and `heights[i] < heights[stack top]`:
     - Pop `top = stack.pop()` — this bar has found its right boundary (`i`).
     - Left boundary = new stack top (or `-1` if stack is empty).
     - Width = `i - left - 1`.
     - Area = `heights[top] * width`.
     - Update `max_size`.
   - Push `i` onto the stack.
3. Return `max_size`.

### Why This Works

- The stack stores indices in **increasing order of height** (bottom to top).
- When `heights[i]` is shorter than the stack top, the stack top has found its **right boundary** (`i`).
- After popping, the new stack top is the **left boundary** — the nearest shorter bar to the left.
- Each bar is pushed and popped exactly once, making this O(n).

### Complexity

- **Time**: O(n) — each element pushed and popped at most once.
- **Space**: O(n) — stack can hold up to n indices in the worst case.

---

## Comparison

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Brute Force (Expand) | O(n²) | O(1) | TLE on large inputs; easy to understand |
| Monotonic Stack | O(n) | O(n) | Optimal; interview standard |

---

## Example

Input:  heights = [2,1,5,6,2,3]

Output: 10

Explanation:
Bar at index 2 (height 5): left boundary = index 1, right boundary = index 4
→ width = 4 - 1 - 1 = 2, area = 5 × 2 = 10 (maximum)

Bar at index 3 (height 6): width = 1, area = 6

Bar at index 1 (height 1): width = 6, area = 6

Largest rectangle area = 10.