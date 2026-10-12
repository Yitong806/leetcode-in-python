from curses.ascii import isalpha, isdigit


class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Time: 06:44.54
        # Date: 2026.10.12
        alphas = [c.lower() for c in s if isalpha(c) or isdigit(c)]
        left, right = 0, len(alphas) - 1
        while left <= right:
            left_alpha, right_alpha = alphas[left], alphas[right]
            if left_alpha != right_alpha:
                return False
            left += 1
            right -= 1
        return True