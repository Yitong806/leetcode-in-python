class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Time: 06:44.54
        # Date: 2026.10.12
        return self.o1_space(s)

    def on_space(self, s: str) -> bool:
        alphas = [c.lower() for c in s if c.isalnum()]
        left, right = 0, len(alphas) - 1
        while left <= right:
            left_alpha, right_alpha = alphas[left], alphas[right]
            if left_alpha != right_alpha:
                return False
            left += 1
            right -= 1
        return True

    def o1_space(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        while left <= right:
            if not s[left].isalnum():
                left += 1
                continue
            if not s[right].isalnum():
                right -= 1
                continue
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True