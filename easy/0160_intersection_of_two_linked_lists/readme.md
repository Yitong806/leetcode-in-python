# 0160. Intersection of Two Linked Lists

## Problem

Given the heads of two singly linked lists `headA` and `headB`, return the node at which the two lists intersect. If the two linked lists have no intersection at all, return `null`.

The intersection is defined based on **reference**, not value — i.e., the two lists share the exact same `ListNode` object from the intersection point onward.

---

## Approach

### O(n) Space: Hash Set

Traverse the first list and store every node reference in a hash set. Then traverse the second list and check whether any node reference has already been recorded. The first match is the intersection point; if the second list is exhausted without a match, there is no intersection.

- **Time**: O(n + m) — each list is traversed once.
- **Space**: O(n) — storing all node references of the first list.

---

### O(1) Space: Two-Pointer Swap (Optimal)

The core idea: if two pointers traverse both lists by **switching to the other list's head upon reaching the end**, they will eventually meet at the intersection — or both become `null` simultaneously if no intersection exists.

#### Why This Works

Let:
- `a` = number of nodes before the intersection in list A
- `b` = number of nodes before the intersection in list B
- `c` = number of shared nodes after the intersection

Pointer `p1` travels `a + c + b` steps total; pointer `p2` travels `b + c + a` steps. Both cover exactly the same total distance. If an intersection exists, they arrive at it at the same time. If not, both reach `null` after `a + b` steps and the loop terminates.

This eliminates the need to precompute lengths or use extra storage.

#### Walkthrough

```
A:  1 → 2 → 3 ↘
                   8 → 9 → 10 → null
B:      4 → 5 ↗
```

- `p1` path: 1→2→3→8→9→10→null → switch to headB → 4→5→8
- `p2` path: 4→5→8→9→10→null → switch to headA → 1→2→3→8
- Both arrive at node `8` simultaneously → intersection found.

**No intersection case**: both pointers travel `len(A) + len(B)` steps, then both become `null`. `p1 is p2` (`null is null`) → loop exits, returns `null`.

---

## Complexity

| Method | Time | Space |
|--------|------|-------|
| Hash Set | O(n + m) | O(n) |
| Two-Pointer Swap | O(n + m) | O(1) |

---

## Key Takeaway

> The two-pointer swap trick equalizes the distance each pointer travels by logically concatenating both lists. It removes the need for length precomputation or extra storage, achieving **O(1) space** with the same linear time complexity.