# 0215. Kth Largest Element in an Array

## Problem

Given an integer array `nums` and an integer `k`, return the **k-th largest** element in the array.

Note that it is the k-th largest element in the sorted order, not the k-th distinct element.

---

## Approach

### O(n log n) Sorting

#### Intuition

The most straightforward approach: sort the array in descending order and directly index the k-th largest element.

#### Algorithm

1. Sort `nums` in descending order.
2. Return `nums[k - 1]`.

#### Complexity

- **Time**: O(n log n) — dominated by the sort.
- **Space**: O(1) extra if the sort is in-place (language-dependent).

This approach is simple and passes within the time limit for most inputs, but doesn't leverage the fact that we only need one element, not a fully sorted array.

---

### O(n log k) Min-Heap (Optimal)

#### Intuition

To find the k-th largest element, we only need to keep track of the **k largest elements seen so far**. A min-heap of size `k` is the ideal structure:

- The heap always contains the k largest elements encountered.
- The **smallest** of those k elements (the heap top) is exactly the k-th largest overall.

#### Algorithm

1. Initialize an empty heap.
2. For each number `n` in `nums`:
   - If the heap has fewer than `k` elements, push `n` directly.
   - Once the heap reaches size `k`, "heapify" it to establish the min-heap property.
   - For subsequent elements: pop the heap minimum, then push back `max(n, popped_value)`. This ensures the heap always retains the larger of the two, gradually filtering out smaller elements.
3. After processing all numbers, the heap top is the k-th largest element.

#### Why It Works

By maintaining a min-heap of the k largest candidates, the root is always the smallest among the top k — which is precisely the k-th largest element in the entire array. Elements smaller than the current k-th largest are progressively discarded and never enter the heap.

#### Walkthrough

`nums = [3, 2, 1, 5, 6, 4]`, `k = 2`

| n | heap state after processing       | action          |
|---|-----------------------------------|-----------------|
| 3 | `[3]`                             | push (size < 2) |
| 2 | `[2, 3]` → heapify → `[2, 3]`     | push, heapify   |
| 1 | pop→1, push max(1,1)=1 → `[2, 3]` | replace         |
| 5 | pop→2, push max(5,2)=5 → `[3, 5]` | replace         |
| 6 | pop→3, push max(6,3)=6 → `[5, 6]` | replace         |
| 4 | pop→5, push max(4,5)=5 → `[5, 6]` | replace         |

Heap top = **5** → 2nd largest ✅

#### Edge Cases

- `k = 1` → returns the maximum element.
- `k = len(nums)` → returns the minimum element.
- All elements identical → returns that element.

---

## Complexity Summary

| Method   | Time       | Space      |
|----------|------------|------------|
| Sorting  | O(n log n) | O(1) extra |
| Min-Heap | O(n log k) | O(k)       |

---

## Key Takeaway

> The min-heap of size k is the canonical pattern for "k-th largest/smallest" problems. It trades a full O(n log n) sort for a targeted O(n log k) partial selection. This approach is especially valuable when `k << n` or when data arrives as a stream (online algorithm). For even better average-case performance, QuickSelect achieves O(n) average time — a common follow-up interview question.