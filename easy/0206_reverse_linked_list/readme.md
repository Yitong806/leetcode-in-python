# 0206. Reverse Linked List

## Problem

Given the `head` of a singly linked list, reverse the list and return the reversed list's head.

---

## Approach: Iterative In-Place Reversal

### Intuition

Reversing a linked list means making every node's `next` pointer point to its predecessor instead of its successor. We can do this in a single pass by maintaining three pointers:

- `prev`: the already-reversed portion's new head (initially `None`)
- `curr`: the current node being processed (starts at `head`)
- `next`: temporarily stores `curr.next` before we overwrite it

At each step, we redirect `curr.next` to point at `prev`, then advance both `prev` and `curr` one step forward.

### Algorithm

1. Initialize `prev = None`, `curr = head`.
2. While `curr` is not `None`:
   - Save `curr.next` in a temporary variable.
   - Point `curr.next` to `prev` (reversing the link).
   - Move `prev` forward to `curr`.
   - Move `curr` forward to the saved next node.
3. When `curr` becomes `None`, `prev` is the new head of the reversed list.

### Why It Works

Each iteration "peels off" one node from the original list and prepends it to the reversed portion. After processing all nodes, the entire list is reversed. No extra data structure is needed — only a constant number of pointer reassignments.

### Walkthrough

`head = 1 → 2 → 3 → None`

| iteration | prev | curr | next (saved) | action | state after |
|-----------|------|------|--------------|--------|-------------|
| 1 | None | 1 | 2 | 1→None | prev=1, curr=2 |
| 2 | 1 | 2 | 3 | 2→1 | prev=2, curr=3 |
| 3 | 2 | 3 | None | 3→2 | prev=3, curr=None |

Return `prev = 3` → `3 → 2 → 1 → None` ✅

### Edge Cases

- Empty list (`head is None`): `prev` stays `None`, returned directly.
- Single node: loop runs once, `1→None` reversed to `1→None`, correct.

---

## Complexity

- **Time**: O(n) — exactly one pass through the list.
- **Space**: O(1) — only three pointers, no recursion, no auxiliary storage.

---

## Key Takeaway

> Linked list reversal is a fundamental building block for many problems (e.g., palindrome check, k-group reversal). The iterative three-pointer pattern is the canonical O(1)-space solution — memorize the `prev / curr / next` dance.