class Solution:
    def jump(self, nums: list[int]) -> int:
        if len(nums) <= 1:
            return 0
        return self.on_greedy(nums)

    def on2_dp(self, nums: list[int]) -> int:
        # accepted
        dp = [999999 for _ in range(len(nums))]
        dp[0] = 0
        for i in range(1, len(dp)):
            for j in range(0, i):
                if nums[j] + j >= i:
                    dp[i] = min(dp[j] + 1, dp[i])

        return dp[-1]

    def on_greedy(self, nums: list[int]) -> int:
        jumps = 0
        current_available_range = 0
        max_available_range = 0
        for i in range(len(nums)):
            if current_available_range >= len(nums) - 1:
                break
            max_available_range = max(i + nums[i], max_available_range)
            if i == current_available_range:
                jumps += 1
                current_available_range = max_available_range

        return jumps