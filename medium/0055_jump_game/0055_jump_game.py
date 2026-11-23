class Solution:
    def canJump(self, nums: list[int]) -> bool:
        if not nums:
            return True
        available_index = 0
        for i in range(0, len(nums)):
            if i > available_index:
                break
            available_index = max(available_index, i + nums[i])

        return available_index >= len(nums) - 1