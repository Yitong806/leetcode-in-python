# 3963. Construct Grid with Exactly One Valid Path

## Problem

You are given two integers `m` and `n`, representing the number of rows and columns of a grid.

Construct any `m x n` grid consisting only of the characters `'.'` (free cell) and `'#'` (obstacle cell), where a valid path is a sequence of free cells that:

- Starts at the top-left cell `(0, 0)`.
- Ends at the bottom-right cell `(m - 1, n - 1)`.
- Moves only right `(i, j) → (i, j + 1)` or down `(i, j) → (i + 1, j)`.

Return any grid such that there is **exactly one** valid path from the top-left cell to the bottom-right cell.

---

## Approach

The key observation is that if we restrict movement to a single L-shaped corridor — **first column down, then last row right** — no branching is possible.

### Construction

1. Initialize all cells to `'#'` (obstacle).
2. Set the entire **first column** (`grid[i][0]` for all `i`) to `'.'`.
3. Set the entire **last row** (`grid[m-1][j]` for all `j`) to `'.'`.

Like this:
```
. # # ... #
. # # ... #
⋮ ⋮ ⋮  ... ⋮ 
. . . ... .     ← last row all '.'
```
### Why Exactly One Path

- At `(0, 0)`, moving right hits `'#'` immediately → only valid move is **down**.
- While on the first column, any right move lands on `'#'` → must continue **down** until `(m-1, 0)`.
- At `(m-1, 0)`, moving down is out of bounds → only valid move is **right**.
- While on the last row, any up move is not allowed (only right/down) → must continue **right** until `(m-1, n-1)`.

The only possible sequence is: **all the way down, then all the way right.** No alternative path can exist because all other cells are obstacles.

### Edge Cases

- `m = 1`: single row, all cells set to `'.'` → exactly one straight-right path.
- `n = 1`: single column, all cells set to `'.'` → exactly one straight-down path.
- Both cases handled naturally by the same construction.

---

## Complexity

- **Time**: O(m × n) — filling the grid.
- **Space**: O(m × n) — output grid storage.