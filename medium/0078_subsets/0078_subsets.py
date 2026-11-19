class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        max111s = pow(2, len(nums))
        ans = []
        for i in range(max111s):
            s = []
            for j in range(len(nums)):
                mask = pow(2, j)
                selection = i & mask
                if selection:
                    s.append(nums[j])

            ans.append(s)
        return ans
