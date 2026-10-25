# 33. Search in Rotated Sorted Array

## Problem

Given a sorted array of integers that has been rotated at an unknown pivot, search for `target` in O(log n) time. Return its index if found, otherwise return `-1`. The array contains distinct values.

---

## Approach: Recursive Binary Search with Sorted Segment Detection

### Intuition

A rotated sorted array is not fully sorted, but **at least one half is always sorted** after any midpoint split. By identifying which half is sorted, we can determine whether `target` lies within that half's range and decide which side to search — achieving O(log n) time without knowing the pivot.

### Algorithm

The solution splits binary search into two modes:

**1. `bisearch_sorted` — Standard Binary Search**

Used when the current segment `[left, right]` is confirmed sorted:
- Compare `target` with `nums[mid]`.
- If equal, return `mid`.
- If `target > nums[mid]`, search right half; otherwise search left half.
- Return `-1` if `left > right`.

**2. `bisearch_unsorted` — Rotated-Aware Binary Search**

Used on segments that may contain the pivot (i.e., not fully sorted):
- Base case: `left > right` → return `-1`.
- Quick checks: test `nums[mid]`, `nums[left]`, `nums[right]` against `target` for early return.
- Determine which half is sorted:
  - **Left half sorted** (`nums[left] < nums[mid]`):
    - If `target` falls within `[nums[left], nums[mid])`, search left using `bisearch_sorted`.
    - Otherwise, recurse on the right half via `bisearch_unsorted`.
  - **Right half sorted** (`nums[left] >= nums[mid]`):
    - If `target` falls within `(nums[mid], nums[right]]`, search right using `bisearch_sorted`.
    - Otherwise, recurse on the left half via `bisearch_unsorted`.

**3. `search` — Entry Point**

Calls `bisearch_unsorted(nums, 0, len(nums) - 1, target)`.

### Why This Works

- In any rotated sorted array, splitting at `mid` always yields at least one contiguous sorted segment.
- A sorted segment allows O(1) range checking: if `target` is within `[sorted_left, sorted_right]`, it must be in that segment; otherwise it must be in the other.
- By alternating between sorted binary search (fast, O(log k)) and unsorted detection (recursive), the algorithm narrows down the search space by half at each step.
- Each recursive call reduces the problem size, maintaining O(log n) overall complexity.

### Edge Cases

- **Target at boundaries**: checked explicitly (`nums[left]`, `nums[right]`) before recursion.
- **Single-element array**: `left == right == mid`, sorted check passes, handled by `bisearch_sorted`.
- **No rotation (fully sorted)**: `nums[left] < nums[mid]` holds throughout, degrades to standard binary search.
- **Target not present**: recursion exhausts all segments and returns `-1`.

---

## Complexity

- **Time**: O(log n) — each call halves the search space; sorted segments use standard binary search (O(log k)).
- **Space**: O(log n) — recursion depth in the worst case (when the array is heavily rotated and each step recurses into the unsorted half).

---

## Alternative (Iterative)

The same logic can be implemented with a `while` loop and no recursion, reducing space to O(1). The recursive version is kept here for clarity of reasoning.