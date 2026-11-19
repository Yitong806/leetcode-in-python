# 0198. House Robber

## Problem

You are a robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses are arranged in a circle? **No — in this version, they are in a line.** (The circular variant is LC 213.)

The constraint: **you cannot rob two adjacent houses**, or the alarm will go off.

Given an integer array `nums` representing the money in each house, return the **maximum amount** you can rob without triggering the alarm.

---

## Approach: Dynamic Programming

### Intuition

At each house `i`, you face a binary decision:
- **Rob house `i`**: then you cannot rob house `i-1`, so your total is `dp[i-2] + nums[i]`
- **Skip house `i`**: then your total is the same as `dp[i-1]`

Therefore:


dp[i] = max(dp[i-1], dp[i-2] + nums[i])


This recurrence captures the optimal substructure: the best outcome at house `i` depends only on the best outcomes at `i-1` and `i-2`.

### Base Cases

- `dp[0] = nums[0]` — only one house, rob it.
- `dp[1] = max(nums[0], nums[1])` — two houses, rob the richer one.

### Algorithm

1. Handle edge cases: empty array → `0`; single house → `nums[0]`.
2. Initialize `dp[0]` and `dp[1]`.
3. For `i` from `2` to `n-1`, apply the recurrence.
4. Return `dp[-1]` (the last element).

### Why It Works

The recurrence explores both choices at every house and picks the better one. By building bottom-up, every subproblem is solved optimally before it is needed — guaranteeing the global optimum via optimal substructure and overlapping subproblems.

### Walkthrough

`nums = [2, 7, 9, 3, 1]`

| i | nums[i] | dp[i-2] + nums[i] | dp[i-1] | dp[i] = max(...) |
|---|---------|-------------------|---------|------------------|
| 0 | 2 | — | — | 2 |
| 1 | 7 | — | — | max(2, 7) = 7 |
| 2 | 9 | 2+9 = 11 | 7 | max(7, 11) = 11 |
| 3 | 3 | 7+3 = 10 | 11 | max(11, 10) = 11 |
| 4 | 1 | 11+1 = 12 | 11 | max(11, 12) = 12 |

Result: **12** (rob houses 0 and 2: 2 + 9 = 11? Wait — 2+9+1 = 12 via houses 0, 2, 4: 2+9+1 = 12 ✅)

### Edge Cases

- Empty `nums` → returns `0`.
- Single house → returns `nums[0]`.
- Two houses → returns `max(nums[0], nums[1])`.
- All negative (not in constraints, but DP still works correctly).

---

## Complexity

- **Time**: O(n) — single pass through the array.
- **Space**: O(n) — storing the full `dp` array.

> **Note**: Since `dp[i]` only depends on `dp[i-1]` and `dp[i-2]`, space can be further optimized to O(1) using two rolling variables — a common follow-up optimization.

---

## Key Takeaway

> House Robber is the canonical "take or skip" DP problem. The pattern — **`dp[i] = max(dp[i-1], dp[i-2] + value[i])`** — generalizes to any scenario where you must choose non-adjacent elements for maximum profit (e.g., stock problems with cooldown, weighted interval scheduling). Always identify the binary choice at each step and express it in terms of earlier subproblems.