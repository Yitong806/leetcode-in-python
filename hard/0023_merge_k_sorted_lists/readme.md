# 0023. Merge k Sorted Lists

## Problem

You are given an array of `k` linked lists, each sorted in ascending order. Merge all the linked lists into one sorted linked list and return its head.

---

## Approach

### O(kn) Brute Force — Repeated Minimum Selection

#### Intuition

There are `N` total nodes across all lists. At each step, scan all `k` list heads to find the node with the smallest value, append it to the result, and advance that list's pointer.

#### Algorithm

1. Compute the total number of nodes `N` across all lists.
2. Initialize an empty result list.
3. Repeat `N` times:
   - Scan all `k` list heads to find the minimum value.
   - Append that node to the result.
   - Advance the corresponding list's head to `head.next`.
4. Return the merged head.

#### Complexity

- **Time**: O(kN) — each of the `N` selections requires scanning `k` heads.
- **Space**: O(1) extra (excluding output list).

This approach is simple but inefficient when `k` is large, as the same minimum-finding work is repeated for every node.

---

### O(N log k) Heap — Priority Queue (Optimal)

#### Intuition

Instead of scanning all `k` heads repeatedly, maintain a min-heap of the current head of each non-empty list. The heap always gives the smallest node in O(log k) time.

#### Algorithm

1. Push the head of every non-empty list into a min-heap, keyed by `(node.val, list_index, node)`. The `list_index` breaks ties deterministically since `ListNode` objects are not comparable.
2. Initialize an empty result list.
3. While the heap is not empty:
   - Pop the smallest node from the heap.
   - Append it to the result.
   - If that node has a `next` node, push `next` into the heap with the same `list_index`.
4. Return the merged head.

#### Why It Works

The heap always contains at most `k` elements (one from each list). Each pop gives the globally smallest available node. By pushing the `next` node back into the heap immediately after popping, we ensure the heap stays current with the leading edge of all lists. This guarantees a fully sorted merge.

#### Walkthrough

`lists = [[1→4→5], [1→3→4], [2→6]]`

| step | heap contents (val, idx) | popped | result so far |
|------|--------------------------|--------|---------------|
| 1 | (1,0), (1,1), (2,2) | 1(idx=0) | 1 |
| 2 | (1,1), (2,2), (4,0) | 1(idx=1) | 1→1 |
| 3 | (2,2), (3,1), (4,0) | 2(idx=2) | 1→1→2 |
| 4 | (3,1), (4,0), (6,2) | 3(idx=1) | 1→1→2→3 |
| 5 | (4,0), (4,1), (6,2) | 4(idx=0) | …→4 |
| 6 | (4,1), (5,0), (6,2) | 4(idx=1) | …→4→4 |
| 7 | (5,0), (6,2) | 5(idx=0) | …→4→4→5 |
| 8 | (6,2) | 6(idx=2) | …→4→4→5→6 |

Result: `1→1→2→3→4→4→5→6` ✅

#### Edge Cases

- All lists empty → heap stays empty → returns `None`.
- Some lists empty → only non-empty heads are pushed.
- Single list → heap has one element, effectively copies the list.

---

## Complexity Summary

| Method | Time | Space |
|--------|------|-------|
| Brute force (repeated min) | O(kN) | O(1) extra |
| Min-heap | O(N log k) | O(k) heap |

Where `N` = total number of nodes across all lists, `k` = number of lists.

---

## Key Takeaway

> Merging k sorted sequences is a canonical heap problem. The pattern — **push all heads into a heap, pop the minimum, push its successor back** — is reusable for any k-way merge (e.g., merging sorted iterators, external sorting, top-k streams). The heap reduces repeated minimum-finding from O(k) to O(log k) per element, which is the critical optimization when k is large.