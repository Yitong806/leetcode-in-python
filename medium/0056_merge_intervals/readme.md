# 0056 Merge Intervals

## Problem
Given an array of intervals where `intervals[i] = [start_i, end_i]`, merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

1. `1 <= intervals.length <= 10^4`
2. `intervals[i].length == 2`
3. `0 <= start_i <= end_i <= 10^4`

## Approach

### Sorting + Linear Scan
The key observation is that if we sort intervals by their start time, overlapping intervals must be adjacent in the sorted order.

1. **Sort** intervals by `start` in ascending order.
2. **Initialize** `current_start` and `current_end` with the first interval.
3. **Iterate** through the remaining intervals:
   - If the current interval's `start` is less than or equal to `current_end`, the two intervals overlap. Extend `current_end` to `max(current_end, interval's end)`.
   - Otherwise, the current merged interval is finalized. Append it to the result, and start a new one with the current interval.
4. **Append** the last merged interval after the loop ends.

The `can_merge` check verifies whether two intervals overlap by comparing the span of their union against the sum of their individual lengths — if the union span is no larger than the sum of lengths, they overlap. After sorting, this simplifies to `interval[i].start <= current_end`.

## Complexity
Time: O(nlogn) for sorting + O(n) for scanning = **O(nlogn)**

Space: O(n) for the output array (excluding input storage)