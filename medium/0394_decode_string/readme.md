# 0394 Decode String

## Problem
Given an encoded string, return its decoded string.
Encoding rule: k[encoded_string], where encoded_string is repeated k times.
Input is always valid; no extra spaces, well-formed brackets.
Output length ≤ 10^5.

## Approach

### Key Insight
Brackets can be nested (e.g. 3[a2[c]]), which means we need to 
"pause" the current decoding, start a new context, and resume later.
This is exactly what a stack is for.

This is critical to solving this problem.

### Algorithm
Maintain a stack of tuples `(current_string, repeat_count)`.

Scan the string from left to right:

1. Digit → build the full number (may be multi-digit)
2. '[' → push `(current_string, repeat_count)` onto stack, 
           then reset current_string="" and repeat_count=0
3. Letter → append to current_string
4. ']' → pop `(prev_string, k)` from stack,
           repeat current_string k times,
           set current_string = prev_string + repeated_string

At the end, current_string is the decoded result.

### Why 2 Stacks Don't Work
Maintaining separate stacks for numbers and strings fails because 
you cannot "reconnect" the correct string context after popping a number.
The tuple approach bundles them together, preserving the full context.

## Complexity
- Time: O(n) — each character is written at most once per nesting level
- Space: O(n) — stack depth + output string