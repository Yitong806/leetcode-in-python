# 0045. Jump Game II

## Problem

You are given a **0-indexed** integer array `nums` where `nums[i]` represents the maximum jump length from index `i`.

Return the **minimum** number of jumps to reach the last index. You can assume that you can always reach the last index.

---

## Approach

### O(n²) DP — Minimum Jumps to Each Position

#### Intuition

Let `dp[i]` be the minimum number of jumps needed to reach index `i`.

To compute `dp[i]`, check every previous index `j` (where `0 ≤ j < i`). If `j` can reach `i` (i.e., `j + nums[j] >= i`), then we can jump from `j` to `i` in one step: