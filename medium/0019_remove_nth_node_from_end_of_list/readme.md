# 19. Remove Nth Node From End of List

## Problem

Given the `head` of a linked list, remove the **n-th node from the end** of the list and return its `head`.

---

## Approach: Two-Pointer (Fast & Slow)

### Intuition

To find the n-th node from the end in a single pass, we use two pointers separated by exactly `n` nodes. When the leading pointer reaches the end, the trailing pointer lands on the node to be removed.

### Algorithm

1. Handle the edge case where `head` is `None` — return `None`.
2. Move `fast` forward `n` steps from `head` using a helper method.
3. Initialize `slow` at `head`. Traverse both pointers together until `fast` reaches the end:
   - When `fast.next is None`, record `slow` as `target_prev` (the node just before the one to remove).
   - Advance both `fast` and `slow` by one step each iteration.
4. After the loop, `slow` is the node to remove (`target`).
5. If `target is head` (i.e., removing the first node), return `head.next`.
6. Otherwise, bypass the target node: `target_prev.next = target.next`.
7. Return `head`.

### Why This Works

By advancing `fast` by `n` steps first, the gap between `fast` and `slow` is `n` nodes. As both move forward together, when `fast` hits the last node, `slow` is exactly `n` nodes behind — i.e., at the n-th node from the end. Tracking `target_prev` during the final iteration gives us the node before it, enabling O(1) removal.

### Edge Cases

- **Removing the head**: when `n` equals the list length, `fast` becomes `None` immediately and `slow` stays at `head`. Handled by the `target is head` check.
- **Single-node list**: returns `None` after `head.next`.
- **n equals list length**: correctly removes the first node.

---

## Complexity

- **Time**: O(n) — at most two passes over the list (one for `jump_n_nodes`, one for the two-pointer traversal). Effectively a single pass.
- **Space**: O(1) — only a constant number of pointers used.