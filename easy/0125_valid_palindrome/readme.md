# 0125 Valid Palindrome

## Problem
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

1. 1 <= `s.length` <= 2 * 10^5
2. s consists only of printable ASCII characters.

## Approach
The solution to this problem is trivial. 

The first version of implementation is :
1. removing all non-alphanumeric chars and changing the rest chars into lower ones, then storing them into a new array. 
2. Just use two pointers to check, while the first one scans from left to right and another one scans from right to left. 
3. Check whether left and right chars match.

Time: O(n), Space: O(n)

However, the new array for storing is quite unnecessary. We can just perform checking on the original string. 
If not alphanumeric chars, just skip it; otherwise, change it into lower one and compare the left char and right char.

Time: O(n), Space: O(1)

## Complexity
- Time: O(n)
- Space: O(1)
