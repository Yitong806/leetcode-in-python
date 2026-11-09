# 0025. Reverse Nodes in k-Group

## Problem

Given the `head` of a linked list, reverse the nodes of the list `k` at a time, and return the modified list.

- `k` is a positive integer.
- If the number of nodes is not a multiple of `k`, then the remaining nodes at the end should stay in their original order.
- You may not alter the values in the list's nodes, only the nodes themselves may be changed.

---

## Approach

The solution splits the linked list into consecutive groups of `k` nodes, reverses each complete group in-place, and then reconnects them.

### Step 1: Identify Groups

Traverse the list and collect each group's `(head, tail)` pair using a helper `jump_k(head, k)` that advances `k-1` steps from a given start. If fewer than `k` nodes remain, that group is left as-is (not reversed).

### Step 2: Reverse Each Group

For every identified `(head, tail)` pair, reverse the sublist from `head` to `tail` in-place using a standard three-pointer reversal (`prev`, `curr`, `next`). The loop stops exactly when `prev` becomes `tail`, ensuring only the target group is reversed.

### Step 3: Reconnect

After reversal, the original `head` of each group becomes its new tail, and the original `tail` becomes its new head. Reconnect groups by linking each new tail (old head) to the next group's new head (old tail). The first group's new head becomes the overall return value.

### Key Details

- **Group boundaries**: After reversal, `head_tails[i][0]` (old head) is the new tail of group `i`, and `head_tails[i][1]` (old tail) is the new head.
- **Final group handling**: If the last group has fewer than `k` nodes, `tail` is `None` and it is not reversed; it is appended directly.
- **Edge cases**: `k = 1` (no reversal needed), list shorter than `k` (return original), empty list (`head is None`).

---

## Complexity

- **Time**: O(n) — each node is visited a constant number of times (once for grouping, once for reversal, once for reconnecting).
- **Space**: O(n/k) — the `head_tails` list stores at most `⌈n/k⌉` pairs of pointers. No recursion stack is used.