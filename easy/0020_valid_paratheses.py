class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        left = ['(', '{', '[']
        left_right_match = {'(': ')', '{': '}', '[': ']'}
        for char in s:
            if char in left:
                stack.append(char)
                continue
            if len(stack) == 0:
                return False
            left_pop = stack.pop()
            if left_right_match[left_pop] != char:
                return False
        return len(stack) == 0