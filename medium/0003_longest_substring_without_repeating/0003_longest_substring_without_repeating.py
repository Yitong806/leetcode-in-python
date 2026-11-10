class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right = 0, 0
        current_set = set()
        longest_length = 0
        while right < len(s):
            while s[right] in current_set:
                current_set.remove(s[left])
                left += 1
            current_set.add(s[right])
            longest_length = max(longest_length, len(current_set))
            right += 1

        return longest_length
