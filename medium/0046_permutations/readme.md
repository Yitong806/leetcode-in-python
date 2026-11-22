# 0046. Permutations

## Problem

Given an array `nums` of **distinct** integers, return all possible permutations. The answer can be returned in **any order**.

---

## Approach: Recursive Insertion

### Intuition

To generate all permutations of `n` elements, we can use a recursive strategy:

1. Take the first element `nums[0]`.
2. Recursively generate all permutations of the remaining elements `nums[1:]`.
3. For each permutation of the remaining elements, insert `nums[0]` at **every possible position** (from index `0` to the end).

This works because inserting the first element into all positions of every permutation of the rest guarantees that the first element appears in every possible slot across all arrangements.

### Algorithm

1. **Base case**: if `nums` has length `1`, return `[nums]` (a single permutation containing just that element).
2. Separate `first = nums[0]` from `rests = nums[1:]`.
3. Recursively call `permute(rests)` to get all permutations of the remaining elements.
4. For each permutation returned:
   - Insert `first` at every index from `0` to `len(permutation)` (inclusive).
   - Append each newly formed permutation to the answer list.
5. Return the answer list.

### Why It Works

A permutation of `n` distinct elements can be constructed by placing any one element in any of `n` positions, with the remaining `n-1` elements filling the rest. By recursively generating permutations of `n-1` elements and inserting the chosen element at every possible slot, we cover all `n!` permutations exactly once.

### Walkthrough

`nums = [1, 2, 3]`

- `permute([1,2,3])` → `first=1`, recurse on `[2,3]`
  - `permute([2,3])` → `first=2`, recurse on `[3]`
    - `permute([3])` → base case → `[[3]]`
  - Insert `2` into `[3]` at positions 0 and 1 → `[[2,3], [3,2]]`
- Insert `1` into each:
  - `[2,3]` → `[1,2,3]`, `[2,1,3]`, `[2,3,1]`
  - `[3,2]` → `[1,3,2]`, `[3,1,2]`, `[3,2,1]`

Result: `[[1,2,3], [2,1,3], [2,3,1], [1,3,2], [3,1,2], [3,2,1]]` ✅ (all 3! = 6 permutations)

### Edge Cases

- Single element `nums = [1]` → returns `[[1]]`.
- Empty array (not in constraints, but would need a separate base case returning `[[]]`).

---

## Complexity

- **Time**: O(n × n!) — there are `n!` permutations, and constructing each takes O(n) for the insertion and list copy.
- **Space**: O(n × n!) — storing all permutations (output size is O(n × n!)); recursion depth is O(n).

---

## Key Takeaway

> The insertion-based recursive approach builds permutations by fixing one element at a time and inserting it into all valid positions of smaller permutations. This is one of several valid strategies (backtracking and BFS-style generation are alternatives), but the insertion method is particularly intuitive: **a permutation of n elements = pick one element × all permutations of the rest with that element inserted everywhere**.