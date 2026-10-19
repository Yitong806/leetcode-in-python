# 0049 Group Anagrams

## Problem
Given an array of strings `strs`, group the **anagrams** together. You can return the answer in any order.

An anagram is a string formed by rearranging the characters of another string, using all the original characters exactly once.

1. `1 <= strs.length <= 10^4`
2. `0 <= strs[i].length <= 100`
3. `strs[i]` consists of lowercase English letters only.

## Approach

### Hash Map with Character Count Tuple as Key

The key insight is that two strings are anagrams **if and only if** they have the exact same character frequency distribution.

For each string:
1. Count the frequency of each character.
2. Convert the `(char, count)` pairs into a **sorted tuple**, which serves as a hashable key uniquely identifying the anagram group.
3. Group strings sharing the same key in a hash map.

After processing all strings, the values of the hash map form the grouped result.

**Why sorted tuple?** A plain `dict` is not hashable. Converting `counts.items()` to a sorted tuple ensures that anagrams like `"eat"` and `"tea"` produce identical keys regardless of iteration order.

**Alternative key strategies:**
- **Sorted string**: `tuple(sorted(s))` — simple but O(k log k) per string where k is string length.
- **Fixed-size count array**: `tuple([0] * 26)` indexed by `ord(c) - ord('a')` — O(k) per string, fastest, but only works for lowercase letters.

## Complexity
Time: O(n · k log k) where n = number of strings, k = average string length (dominated by sorting character counts)

Space: O(n · k) for storing the hash map and keys