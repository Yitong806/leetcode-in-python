# 81. Search in Rotated Sorted Array II

## Problem

Given an integer array `nums` sorted in non-decreasing order (with **possible duplicate values**), which has been rotated at an unknown pivot, return `true` if `target` exists in `nums`, otherwise return `false`.

---

## Approach: Recursive Binary Search with Duplicate Handling

### Intuition

This problem extends [LC 33](../0033_search_in_rotated_sorted_array/) by allowing duplicate elements. In a rotated sorted array, splitting at `mid` always yields at least one sorted half — except when `nums[left] == nums[mid]`, where duplicates make it impossible to determine which half is sorted. In that case, we skip `left` by one position and retry.

### Algorithm

Three methods compose the solution:

**1. `search` — Entry Point**

Converts the index result from `_search` into a boolean: `return _search(nums, target) != -1`.

**2. `_bisearch_sorted` — Standard Binary Search**

Used when the current segment `[left, right]` is confirmed sorted:
- Compare `target` with `nums[mid]`.
- If equal, return `mid`.
- If `target > nums[mid]`, search right half; otherwise search left half.
- Return `-1` if `left > right`.

**3. `_bisearch_unsorted` — Rotated-Aware Binary Search (Recursive)**

Used on segments that may contain the pivot:
- Base case: `left > right` → return `-1`.
- Quick checks: test `nums[mid]`, `nums[left]`, `nums[right]` against `target` for early return.
- Determine which half is sorted:
  - **Left half sorted** (`nums[left] < nums[mid]`):
    - If `nums[left] < target < nums[mid]`, search left using `_bisearch_sorted`.
    - Otherwise, recurse on the right half via `_bisearch_unsorted`.
  - **Right half sorted** (`nums[left] > nums[mid]`):
    - If `nums[mid] < target < nums[right]`, search right using `_bisearch_sorted`.
    - Otherwise, recurse on the left half via `_bisearch_unsorted`.
  - **`nums[left] == nums[mid]`** (cannot determine which half is sorted):
    - Skip `left` by calling `_bisearch_unsorted(nums, left + 1, right, target)`.

**4. `_search` — Wrapper**

Calls `_bisearch_unsorted(nums, 0, len(nums) - 1, target)`.

### Why This Works

- When `nums[left] < nums[mid]` or `nums[left] > nums[mid]`, at least one half is strictly sorted, enabling O(1) range checking to decide which side to search.
- When `nums[left] == nums[mid]`, duplicates prevent determining order. Incrementing `left` by 1 eliminates one ambiguous element; on the next recursive call, `mid` is recomputed and ordering becomes distinguishable.
- Each recursive call either halves the search space (clear ordering) or reduces it by 1 (duplicate ambiguity), guaranteeing progress.

### Edge Cases

- **All elements identical** (e.g., `[1,1,1,1]`): `left` increments one by one, degrades to O(n).
- **`target` at boundaries**: checked explicitly (`nums[left]`, `nums[right]`) before recursion.
- **Single-element array**: `left == right == mid`, `nums[mid] == target` caught immediately.
- **No rotation (fully sorted)**: `nums[left] < nums[mid]` holds, degrades to standard binary search via `_bisearch_sorted`.

---

## Complexity

- **Time**: O(n) worst case (all duplicates); O(log n) average case.
- **Space**: O(n) worst case (recursion depth when `left` increments one by one); O(log n) average.