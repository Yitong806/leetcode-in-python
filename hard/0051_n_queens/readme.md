# 0051. N-Queens

## Problem

The n-queens puzzle is the problem of placing `n` queens on an `n x n` chessboard such that no two queens attack each other.

Given an integer `n`, return all distinct solutions to the n-queens puzzle. Each solution contains a distinct board configuration of the `n`-queens' placement, where `'Q'` indicates a queen and `'.'` indicates an empty space.

---

## Approach: DFS Backtracking with Availability Matrix

### Intuition

Place queens row by row. At each row, try every column position. Before placing a queen, check whether that position is under attack by any previously placed queen. If safe, place it and recurse to the next row. After exploring all branches, backtrack by removing the queen and trying the next column.

### Availability Check

Instead of checking conflicts on the fly, the implementation pre-computes an availability matrix for the entire board based on all currently placed queens:

- A queen attacks along **8 directions**: horizontal, vertical, and all four diagonals.
- For each placed queen, mark its position and every square reachable along all 8 directions as unavailable (until the board boundary is hit).
- A candidate position `(row, col)` is valid only if the availability matrix says `True` at that coordinate.

This approach recomputes the full availability matrix from scratch at each decision point — straightforward and correct, though not the most optimized conflict-checking strategy.

### Algorithm

1. Initialize an `n x n` chessboard with all zeros (no queens placed).
2. Call `dfs(chessboard, current_row, n)`:
   - **Base case**: if `current_row == n`, all queens are placed successfully. Convert the board to string format and add to the answer list.
   - **Recursive case**: for each column `i` in the current row:
     - If `current_available(current_row, i)` is `True`, place a queen at `(current_row, i)`.
     - Recurse to `current_row + 1`.
     - Backtrack: remove the queen (set back to `0`).
3. Return all collected solutions.

### Board-to-String Conversion

Each integer board (where `1` = queen, `0` = empty) is converted to a list of strings: `'Q'` for a queen, `'.'` for empty.

### Walkthrough (n = 4)

Two valid solutions exist:


Solution 1:          Solution 2:
.Q..                 ..Q.
...Q                 Q...
Q...                 ...Q
..Q.                 .Q..


The DFS explores all placements row by row, pruning branches where a queen would be attacked, and backtracking to discover both valid configurations.

### Edge Cases

- `n = 1` → returns `[["Q"]]`.
- `n = 2` or `n = 3` → returns `[]` (no valid placement exists).

---

## Complexity

- **Time**: O(n!) in the best case with pruning, but the availability matrix recomputation adds O(n²) per call, making each level more expensive. Overall it is bounded by O(n² × n!) for the naive availability check.
- **Space**: O(n²) for the chessboard and availability matrix, plus O(n!) storage for all solutions in the output.

> **Note**: More optimized approaches use boolean arrays for columns and diagonals (O(1) conflict check per position), reducing per-step overhead significantly. The availability matrix approach trades efficiency for conceptual clarity.

---

## Key Takeaway

> N-Queens is the canonical backtracking problem. The pattern — **try a choice → recurse → undo the choice** — applies to any constraint-satisfaction puzzle. The key design decisions are: (1) how to represent state, and (2) how to efficiently check constraints. Simpler conflict-checking logic (like an availability matrix) is easier to verify; optimized versions (sets for columns/diagonals) are faster but require more careful indexing.