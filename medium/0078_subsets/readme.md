# 0078. Subsets

## Problem

Given an integer array `nums` of **unique** elements, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. The subsets can be returned in **any order**.

---

## Approach: Bitmask Enumeration

### Intuition

A set of `n` elements has exactly `2^n` subsets. Each element has exactly two choices: **included** or **excluded**. This binary choice maps naturally to a bitmask of length `n`.

For each integer `i` from `0` to `2^n - 1`:
- Treat `i` as a bitmask where the `j`-th bit represents whether `nums[j]` is included.
- If the `j`-th bit of `i` is `1`, include `nums[j]` in the current subset.

### Algorithm

1. Compute `total = 2^n` (the number of subsets).
2. For each `i` in `[0, total - 1]`:
   - Initialize an empty subset.
   - For each bit position `j` from `0` to `n-1`:
     - If `i & (1 << j)` is non-zero, append `nums[j]` to the subset.
   - Add the subset to the answer list.
3. Return the answer list.

### Why It Works

Every integer from `0` to `2^n - 1` represents a unique combination of `n` binary choices. Iterating through all such integers guarantees that every possible subset is generated exactly once — no more, no less.

### Walkthrough

`nums = [1, 2, 3]`, `n = 3`, `total = 8`

| i | binary | bits set | subset |
|---|--------|----------|--------|
| 0 | 000 | none | `[]` |
| 1 | 001 | bit 0 | `[1]` |
| 2 | 010 | bit 1 | `[2]` |
| 3 | 011 | bits 0,1 | `[1, 2]` |
| 4 | 100 | bit 2 | `[3]` |
| 5 | 101 | bits 0,2 | `[1, 3]` |
| 6 | 110 | bits 1,2 | `[2, 3]` |
| 7 | 111 | bits 0,1,2 | `[1, 2, 3]` |

Result: `[[], [1], [2], [1,2], [3], [1,3], [2,3], [1,2,3]]` ✅

### Edge Cases

- Empty `nums = []` → returns `[[]]` (the empty set is a valid subset; `2^0 = 1`).
- Single element `nums = [1]` → returns `[[], [1]]`.

---

## Complexity

- **Time**: O(n × 2^n) — there are `2^n` subsets, and constructing each takes O(n) to check all bits.
- **Space**: O(n × 2^n) — storing all subsets (output size itself is O(n × 2^n)).

---

## Key Takeaway

> Bitmask enumeration is the most straightforward way to generate all subsets. It avoids recursion and backtracking, making the logic easy to verify — each subset corresponds to exactly one integer. For problems involving "all combinations of choices," bitmask is often the cleanest mental model, even if backtracking is more space-efficient in practice.