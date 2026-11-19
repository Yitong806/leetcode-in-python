# 0070. Climbing Stairs

## Problem

You are climbing a staircase with `n` steps. Each time you can either climb `1` step or `2` steps. Return the number of **distinct ways** to reach the top.

---

## Approach: Dynamic Programming → Fibonacci

### Intuition

Let `dp[i]` be the number of distinct ways to reach step `i`.

To reach step `i`, you can come from:
- Step `i-1` (by taking a single step of size 1)
- Step `i-2` (by taking a single step of size 2)

Therefore:


dp[i] = dp[i-1] + dp[i-2]


This is exactly the **Fibonacci recurrence**. The base cases are:
- `dp[1] = 1` (only one way: take 1 step)
- `dp[2] = 2` (two ways: 1+1 or 2)

### Space Optimization

Since `dp[i]` only depends on the previous two values, we don't need an array. Two variables `a` and `b` are sufficient:
- `a` represents `dp[i-2]`
- `b` represents `dp[i-1]`
- At each step: `a, b = b, a + b`

After iterating from `2` to `n-1`, `b` holds `dp[n]`.

### Why This Works

Every path to step `n` is uniquely determined by the sequence of 1-steps and 2-steps that sum to `n`. The number of such compositions follows the Fibonacci sequence — a classic combinatorial result. The DP formulation captures this naturally by decomposing the problem into the last move taken.

### Walkthrough

`n = 5`

| i | a (dp[i-2]) | b (dp[i-1]) | new b = a + b |
|---|-------------|-------------|---------------|
| 2 | 1           | 2           | 3             |
| 3 | 2           | 3           | 5             |
| 4 | 3           | 5           | 8             |

Result: **8** distinct ways.

Verification: compositions of 5 using 1s and 2s:
`1+1+1+1+1`, `2+1+1+1`, `1+2+1+1`, `1+1+2+1`, `1+1+1+2`, `2+2+1`, `2+1+2`, `1+2+2` → 8 ✅

### Edge Cases

- `n = 1` → returns `1` (only one step).
- `n = 2` → returns `2` (1+1 or 2).
- `n = 0` → not in constraints (n ≥ 1), but would logically be `1` (one way: do nothing).

---

## Complexity

- **Time**: O(n) — single loop from 2 to n-1.
- **Space**: O(1) — only two integer variables.

---

## Key Takeaway

> Climbing Stairs is the canonical introduction to DP. The pattern `dp[i] = dp[i-1] + dp[i-2]` appears in many disguised forms — any problem where the solution at step `i` depends on the two previous steps follows the same Fibonacci-like structure. Always ask: *"Can I express this in terms of smaller subproblems?"*