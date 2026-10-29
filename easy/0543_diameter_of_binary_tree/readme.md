# Problem: 543. Diameter of Binary Tree

## Core Concept
The diameter of a binary tree is the maximum number of edges along any path between two nodes. The longest path always passes through some node's left and right subtrees. 

## Approach (DFS / Recursion):
Instead of finding paths, we calculate the **height** of each subtree. For any given node:
1. The longest path passing *through* this node = `left_height + right_height` (in edges).
2. The height returned to its parent = `max(left_height, right_height) + 1`.

By traversing every node (post-order DFS), we update a global variable to track the maximum diameter found.

**Complexity**:
- Time: O(n) — visit every node once.
- Space: O(h) — recursion stack, where h is tree height (O(n) worst case, O(log n) balanced).