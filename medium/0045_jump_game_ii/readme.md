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


dp[i] = min(dp[i], dp[j] + 1)


#### Algorithm

1. Initialize `dp` with a large value (`∞`), set `dp[0] = 0`.
2. For each `i` from `1` to `n-1`:
   - For each `j` from `0` to `i-1`:
     - If `j + nums[j] >= i`, update `dp[i] = min(dp[i], dp[j] + 1)`.
3. Return `dp[n-1]`.

#### Complexity

- **Time**: O(n²) — nested loops over all pairs.
- **Space**: O(n) — DP array.

This approach is correct but will TLE on large inputs. It establishes the optimal substructure: the minimum jumps to `i` depends on all reachable predecessors.

---

### O(n) Greedy — BFS-Like Range Expansion (Optimal)

#### Intuition

Instead of computing minimum jumps to every single index, think in terms of **ranges**:

- `current_available_range`: the farthest index reachable with exactly `jumps` jumps.
- `max_available_range`: the farthest index reachable if we take one more jump from anywhere within the current range.

As we iterate through the array:
- We continuously update `max_available_range` with `max(max_available_range, i + nums[i])`.
- When we reach the boundary of the `current_available_range`, it means we've explored all options within the current jump count. We **must** take another jump:
  - Increment `jumps`.
  - Extend `current_available_range` to `max_available_range`.

This is equivalent to a **level-by-level BFS** on a graph, but done in O(1) space.

#### Why It Works

Within the current reachable range, we've seen all possible jump options. The best next landing point is the one that extends our reach the farthest. By only incrementing the jump counter when we hit the current boundary, we guarantee the minimum number of jumps — each jump takes us as far as possible.

#### Walkthrough

`nums = [2, 3, 1, 1, 4]`

| i | nums[i] | i + nums[i] | max_available_range | current_available_range | jumps | action |
|---|---------|-------------|---------------------|-------------------------|-------|--------|
| 0 | 2 | 2 | 2 | 0 | 0 | i==0, jump→1, range→2 |
| 1 | 3 | 4 | 4 | 2 | 1 | — |
| 2 | 1 | 3 | 4 | 2 | 1 | i==2, jump→2, range→4 |
| 3 | 1 | 4 | 4 | 4 | 2 | — |
| 4 | 4 | 8 | 8 | 4 | 2 | i==4 ≥ n-1, break |

Result: **2** jumps (0→1→4 or 0→2→4) ✅

`nums = [1, 1, 1, 1]`

| i | i+nums[i] | max_range | curr_range | jumps |
|---|-----------|-----------|------------|-------|
| 0 | 1 | 1 | 0→jump→1 | 1 |
| 1 | 2 | 2 | 1→jump→2 | 2 |
| 2 | 3 | 3 | 2→jump→3 | 3 |
| 3 | 4 | 4 | 3≥n-1, break | — |

Result: **3** jumps ✅

#### Edge Cases

- `len(nums) <= 1` → returns `0` (already at destination).
- Already guaranteed to reach the end (per problem constraints).

---

## Complexity Summary

| Method | Time | Space |
|--------|------|-------|
| DP | O(n²) | O(n) |
| Greedy (range expansion) | O(n) | O(1) |

---

## Key Takeaway

> Jump Game II is the natural follow-up to Jump Game (LC 55). While LC 55 only asks *whether* you can reach the end (greedy reachability), LC 45 asks for the *minimum* jumps. The key insight is to think in **ranges, not positions** — each jump should take you as far as possible within the current reachable window. This BFS-like greedy strategy collapses an O(n²) DP into a single O(n) pass with O(1) space.