# 0042 Trapping Rain Water

## Problem
Given `n` non-negative integers representing an elevation map where the width of each bar is `1`, compute how much water it can trap after raining.

1. `n == height.length`
2. `1 <= n <= 2 * 10^4`
3. `0 <= height[i] <= 10^5`

## Approach

### 1. Brute Force — O(n²)
For each bar `i` (excluding the two ends), scan left to find the maximum height on its left, and scan right to find the maximum height on its right. The water trapped at `i` is `min(left_max, right_max) - height[i]` (if positive).

- Time: O(n²)
- Space: O(1)

### 2. Precomputed Left/Right Max Arrays — O(n)
Instead of scanning left and right for every bar, precompute two arrays in a single pass each:
- `left_max[i]` = maximum height from index `0` to `i`
- `right_max[i]` = maximum height from index `i` to `n-1`

Then for each bar, trapped water = `min(left_max[i], right_max[i]) - height[i]`.

- Time: O(n)
- Space: O(n)

### 3. Two Pointers — O(n) Time, O(1) Space
The optimal approach. Key insight: **the amount of water trapped at a position depends on the shorter of the two boundary maxima.** If `height[left] < height[right]`, then the left side's `left_max` is the bottleneck — we can compute water for `left` without knowing the exact `right_max`, because `right_max >= height[right] > height[left] >= left_max`, so `min(left_max, right_max) = left_max`.

We maintain two pointers `left` and `right`, and two running maxima `left_max` and `right_max`:
- If `height[left] < height[right]`: water at `left` is `left_max - height[left]`; move `left` rightward.
- Otherwise: water at `right` is `right_max - height[right]`; move `right` leftward.

This eliminates the need for extra arrays while preserving correctness.

- Time: O(n)
- Space: O(1)

## Complexity
- **Time**: O(n) for both the precomputed array and two-pointer approaches.
- **Space**: O(1) for two pointers.