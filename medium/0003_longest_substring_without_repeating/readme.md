# 0003. Longest Substring Without Repeating Characters

## Problem

Given a string `s`, find the length of the **longest substring** without duplicate characters.

---

## Approach: Sliding Window with Hash Set

Maintain a window `[left, right]` that always contains **no repeating characters**. A set `current_set` tracks which characters are currently inside the window.

### Algorithm

1. Initialize `left = 0`, `right = 0`, `current_set = ∅`, `longest_length = 0`.
2. Expand the window by moving `right` forward one character at a time.
3. Before adding `s[right]`, if it already exists in `current_set`, shrink the window from the left: remove `s[left]` and increment `left` until `s[right]` is no longer in the set.
4. Add `s[right]` to `current_set` and update `longest_length = max(longest_length, len(current_set))`.
5. Repeat until `right` reaches the end of the string.

### Why It Works

- The window invariant is: **all characters in `[left, right]` are distinct**.
- When a duplicate is detected (`s[right]` already in set), we shrink from the left until the duplicate is removed. This guarantees the window is always valid.
- Every time we add a new character, the window represents the longest valid substring **ending at `right`**. Tracking the maximum over all `right` gives the answer.

### Example Walkthrough

`s = "abcabcbb"`:

| right | char | window before shrink | after shrink | current_set | longest |
|-------|------|---------------------|--------------|-------------|---------|
| 0 | a | — | `[0,0]` | `{a}` | 1 |
| 1 | b | — | `[0,1]` | `{a,b}` | 2 |
| 2 | c | — | `[0,2]` | `{a,b,c}` | 3 |
| 3 | a | `[0,3]` has dup | shrink to `[1,3]` | `{b,c,a}` | 3 |
| 4 | b | `[1,4]` has dup | shrink to `[2,4]` | `{c,a,b}` | 3 |
| 5 | c | `[2,5]` has dup | shrink to `[3,5]` | `{a,b,c}` | 3 |
| 6 | b | `[3,6]` has dup | shrink to `[4,6]` | `{c,a,b}` | 3 |
| 7 | b | `[4,7]` has dup | shrink to `[7,7]` | `{b}` | 3 |

Result: **3** (substring `"abc"`).

### Edge Cases

- Empty string `""` → returns `0`.
- All identical chars `"bbbb"` → window shrinks to size 1 each step, returns `1`.
- All distinct `"abcd"` → window never shrinks, returns `len(s)`.

---

## Complexity

- **Time**: O(n) — `left` and `right` each move at most `n` times; set operations are O(1) average.
- **Space**: O(min(m, n)) — the set holds at most `m` distinct characters (where `m` is the size of the character set, e.g., 26 for lowercase letters, 128 for ASCII, or up to `n` in worst case).