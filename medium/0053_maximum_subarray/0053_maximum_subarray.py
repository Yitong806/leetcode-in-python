class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        if not nums:
            return 0
        return self.on3_brute_force(nums)

    def on3_brute_force(self, nums: list[int]) -> int:
        ans = nums[0]
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                curr = 0
                for k in range(i, j + 1):
                    curr += nums[k]
                ans = max(ans, curr)

        return ans

    def on2_brute_force(self, nums: list[int]) -> int:
        ans = nums[0]
        for i in range(len(nums)):
            current_sum = 0
            for j in range(i, len(nums)):
                current_sum += nums[j]
                ans = max(ans, current_sum)

        return ans

    def on_space_dp(self, nums: list[int]) -> int:
        dp = [0 for _ in range(len(nums))]
        dp[0] = nums[0]
        for i in range(1, len(nums)):
            dp[i] = max(dp[i-1]+nums[i], nums[i])

        return max(dp)

    def o1_space_dp(self, nums: list[int]) -> int:
        ans = current = nums[0]
        for i in range(1, len(nums)):
            current = max(current + nums[i], nums[i])
            ans = max(current, ans)
        return ans