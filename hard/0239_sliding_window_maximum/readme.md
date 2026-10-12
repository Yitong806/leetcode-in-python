# 0239 Sliding Window Maximum

## Problem
You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

Return the max sliding window.

Constraints:
1. 1 <= nums.length <= 10^5
2. -10^4 <= nums[i] <= 10^4
3. 1 <= k <= nums.length

## Approach

### Brute Force
This is easy to implement but quite time-consuming while running.

Just check every sliding window then calculate the maximum of each one.

Time complexity: O(nk)
Space complexity: O(k)

This can only pass 38/53 testcases.

### Priority Queue (Heap + Lazy Deletion)

The key observation is: we need a data structure that can efficiently tell us the maximum in the current window. A max-heap fits naturally, but the challenge is removing elements that slide out of the window.

Standard heaps do not support efficient deletion by value or index. Instead of fighting this limitation, we use **lazy deletion**:

- Maintain a max-heap storing `(-value, index)` pairs (Python's `heapq` is a min-heap, so we negate values)
- For each new element, push it onto the heap
- Before reading the heap top, pop all entries whose index has fallen out of the current window (`index <= i - k`)
- The heap top is guaranteed to be the maximum of the current window

This way, each element is pushed once and popped at most once.

Time complexity: O(n log k) — each of the n elements is pushed and popped at most once
Space complexity: O(k) — heap stores at most k+1 elements

Note: We cannot simply delete a specific element from the heap in O(log k) because the heap does not expose element positions. Lazy deletion sidesteps this entirely.

### Monotonic Queue (Optimal)

The optimal solution uses a **deque (double-ended queue)** to maintain a decreasing sequence of candidate maximums.

Key idea: at any moment, only elements that could become the maximum in future windows matter. If a new element is larger than some existing candidates, those smaller candidates will never be the maximum while the new element is still in the window — so we evict them.

Algorithm:
1. Maintain a deque storing **indices** of elements in decreasing order of their values
2. For each element at index `i`:
   - **Evict smaller elements**: while deque is not empty and `nums[i] >= nums[deque[-1]]`, pop from the back
   - **Enqueue**: append `i` to the back
   - **Evict out-of-window**: if `deque[0] <= i - k`, pop from the front
   - **Record result**: once `i >= k - 1`, `nums[deque[0]]` is the current window maximum

Why this works:
- The deque front always holds the index of the current maximum
- Elements are evicted only when they are permanently shadowed by a larger element that outlives them in the window
- Each element enters and leaves the deque at most once

Time complexity: O(n) — each element is pushed and popped at most once

Space complexity: O(k) — deque holds at most k indices

### Comparison

| Approach | Time | Space | Difficulty |
|----------|------|-------|------------|
| Brute Force | O(nk) | O(k) | Trivial |
| Priority Queue (Lazy Deletion) | O(n log k) | O(k) | Easy |
| Monotonic Queue | O(n) | O(k) | Medium |
