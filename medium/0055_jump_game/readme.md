# 0055. Jump Game

## Problem

You are given an integer array `nums` where `nums[i]` represents the maximum jump length from index `i`. Starting at index `0`, return `true` if you can reach the last index, and `false` otherwise.

---

## Approach: Greedy — Track Farthest Reachable Index

### Intuition

At each position `i`, we can jump up to `nums[i]` steps forward. The key observation is that we don't need to know the exact path taken — we only need to know the **farthest index** reachable so far.

If at any point the current index `i` exceeds the farthest reachable index, it means we cannot physically reach `i` (and therefore anything beyond it) → the game is unwinnable from that point onward.

If the farthest reachable index ever reaches or surpasses the last index, we can reach the destination.

### Algorithm

1. Initialize `available_index = 0` (the farthest index reachable from any position visited so far).
2. Iterate `i` from `0` to `n-1`:
   - If `i > available_index`, break — we've hit a gap we cannot cross.
   - Update `available_index = max(available_index, i + nums[i])`.
3. After the loop, return `available_index >= len(nums) - 1`.

### Why It Works

The greedy choice is safe because:
- Jump lengths are **maximums** — if you can jump at least `k` steps, you can also jump fewer. So reaching a farther index never hurts.
- We only need existence of *a* valid path, not the optimal one. Tracking the farthest reachable index monotonically captures all possibilities.

### Walkthrough

`nums = [2, 3, 1, 1, 4]`

| i | nums[i] | i + nums[i] | available_index (after update) | i > available_index? |
|---|---------|-------------|-------------------------------|----------------------|
| 0 | 2 | 2 | 2 | No |
| 1 | 3 | 4 | 4 | No |
| 2 | 1 | 3 | 4 | No |
| 3 | 1 | 4 | 4 | No |
| 4 | 4 | 8 | 8 | No (loop ends) |

`available_index = 8 >= 4` → **true** ✅

`nums = [3, 2, 1, 0, 4]`

| i | nums[i] | i + nums[i] | available_index | i > available_index? |
|---|---------|-------------|-----------------|----------------------|
| 0 | 3 | 3 | 3 | No |
| 1 | 2 | 3 | 3 | No |
| 2 | 1 | 3 | 3 | No |
| 3 | 0 | 3 | 3 | No |
| 4 | 4 | 8 | — | **Yes (4 > 3)** → break |

Loop breaks at `i = 4` → `available_index = 3 < 4` → **false** ✅

### Edge Cases

- Empty `nums` → returns `true` (no jumps needed).
- Single element `nums = [0]` → `available_index = 0 >= 0` → `true`.
- All zeros → only reachable if `n = 1`; otherwise `false` (unless a prior jump covers the gap).

---

## Complexity

- **Time**: O(n) — single pass through the array.
- **Space**: O(1) — only one integer variable.

---

## Key Takeaway

> Jump Game demonstrates that a greedy strategy can often replace DP when the optimal substructure allows it. The core principle — **"track the farthest reachable boundary and bail as soon as you hit a gap"** — is reusable in interval-covering problems (e.g., Jump Game II, gas station, merging intervals). Always ask: *"Do I need the exact path, or just reachability?"*