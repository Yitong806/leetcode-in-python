class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        if len(nums) == 1:
            return [nums]
        rests = [nums[i] for i in range(1, len(nums))]
        first = nums[0]
        ans = []
        rests_permutation = self.permute(rests)
        for r_p in rests_permutation:
            for i in range(0, len(r_p) + 1):

                r_p_clone = [v for v in r_p]
                r_p_clone.insert(i, first)

                ans.append(r_p_clone)

        return ans
