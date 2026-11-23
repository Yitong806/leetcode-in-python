# 0079. Word Search

## Problem

Given an `m x n` grid of characters `board` and a string `word`, return `true` if `word` can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

---

## Approach: DFS Backtracking

### Intuition

We need to find whether the given `word` can be formed by walking through adjacent cells on the board without revisiting any cell. This is a classic path-search problem on a 2D grid, naturally solved by depth-first search with backtracking.

### Algorithm

1. **Pre-filter starting positions**: Instead of trying every cell on the board, first collect all positions where `board[i][j] == word[0]`. This prunes obviously invalid branches early.
2. **DFS from each candidate start**:
   - Mark the current cell as `visited`.
   - If `index == len(word)`, the entire word has been matched → return `true`.
   - Otherwise, try all 4 directions (up, right, down, left):
     - Check boundary validity.
     - Check that the neighbor matches `word[index]`.
     - Check that the neighbor has not been visited.
     - Recurse with `index + 1`.
     - Backtrack: unmark the neighbor as visited.
   - If any direction leads to success, propagate `true` upward.
3. If all starting positions are exhausted without success, return `false`.

### Why It Works

The DFS explores every possible path starting from each valid starting cell. The `visited` matrix guarantees no cell is reused within a single path. Backtracking ensures that different branches don't interfere with each other's state. Since we only move to neighbors that match the expected character, invalid paths are pruned immediately.

### Walkthrough

`board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]`, `word = "ABCCED"`

- Starting positions for `'A'`: `(0,0)` and `(2,0)`.
- From `(0,0)`:
  - `A` → right to `B` → right to `C` → down to `C` → down to `E` → left to `D` ✅
  - Path: `(0,0)→(0,1)→(0,2)→(1,2)→(2,2)→(2,1)`
- Returns `true`.

### Edge Cases

- Empty `word` → returns `true` (by definition, an empty string is always present).
- `word` length = 1 → checks if any cell matches that single character.
- No valid path → returns `false`.

---

## Complexity

- **Time**: O(m × n × 4^L) in the worst case, where `L = len(word)`. From each starting cell, the DFS branches up to 4 ways for `L-1` levels. The pre-filter step is O(m × n).
- **Space**: O(L) for the recursion stack (maximum depth equals word length), plus O(m × n) for the `visited` matrix.

> **Note**: In practice, the search is much faster due to character-mismatch pruning — branches die as soon as the next character doesn't match.

---

## Key Takeaway

> Word Search is the canonical 2D grid DFS + backtracking problem. The pattern — **pre-filter starts → DFS with visited tracking → backtrack on return** — applies to any grid-based path-finding problem (e.g., flood fill, island counting, maze solving). The key is maintaining clean state isolation between branches through careful backtracking.