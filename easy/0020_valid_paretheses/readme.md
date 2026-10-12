# 0020 Valid Parentheses

## Problem
Given a string s containing just ```()[]{}```, determine if it's valid.
Valid if: open/close match, correct order, every close has a matching open.

1. 1 <= ```s.length``` <= 10^4
2. s consists of parentheses only ```()[]{}```.

## Approach
This problem is a classical algorithm in the Stack and Queue part of Data Structure and Algorithm Analysis(DSAA). 

As introduced in DSAA, this problem can be solved via:

Use a stack to track unmatched opening brackets.

1. Scan s left to right
2. If ```({[``` → push onto stack
3. If ```)}]``` → 
   - If stack is empty → return false
   - Pop top, check if it matches the closing bracket
   - Mismatch → return false
4. After scanning, return stack.empty()

## Complexity
- Time: O(n)
- Space: O(n)
