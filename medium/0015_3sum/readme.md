# 0015 3Sum

## Problem
Given an integer array nums, return all the triplets `[nums[i], nums[j], nums[k]]` such that `i != j`, `i != k`, and `j != k`, and `nums[i] + nums[j] + nums[k] == 0`.

Notice that the solution set must not contain duplicate triplets.

1. 3 <= `nums.length` <= 3000
2. -10^5 <= `nums[i]` <= 10^5

## Approach

### Brute Force
This is trivial. Just use 3-level for to check all possible triples.

Use a set to deduplicate the triples in tuple forms.

Time: O(n^3), Space: O(n)

TLE, 311/316 passed.

### Dual Pointers

Brute force enumerates all triplets, resulting in massive redundant comparisons (the same value is repeatedly paired with different elements). We can eliminate this by sorting first.

1. **Sort the array** so that equal values become adjacent, which is the prerequisite for both deduplication and pointer movement.
2. **Fix one number `nums[i]`**, then use two pointers in the remaining range `[i+1, n-1]` to find the other two:
   - `nums[i] + nums[left] + nums[right] == 0` → record the triplet, then `left++` and `right--`
   - Sum `< 0` → `left++` (need a larger value)
   - Sum `> 0` → `right--` (need a smaller value)
3. **Deduplication**: after each step, skip consecutive identical values for `i`, `left`, and `right` to avoid duplicate triplets in the result.

Sorting takes O(nlogn). The outer loop scans O(n) and the inner two-pointer scan is O(n), giving total O(n^2). Extra space comes from the sorting routine (depending on the algorithm) and the result list.

- Time: O(n^2)
- Space: O(logn) ~ O(n) (sorting stack + result storage)

## Complexity
- Time: O(n^2)
- Space: O(n)
