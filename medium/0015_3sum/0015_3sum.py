class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        # Time: 19:25.82
        # Date: 2026.10.12
        return self.on3_brute_force(nums)

    def on3_brute_force(self, nums: list[int]) -> list[list[int]]:
        n = len(nums)
        triples = set()
        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                for k in range(j + 1, n):
                    if nums[i]+nums[j]+nums[k] == 0:
                        l = [nums[i], nums[j], nums[k]]
                        l.sort()
                        triples.add(tuple(l))

        return list(triples)

    def on2_dual_pointers(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        triples = set()
        for i in range(len(nums) - 2):
            left = i + 1
            right = len(nums) - 1

            while left < right:
                sum3 = nums[i] + nums[left] + nums[right]
                if sum3 == 0:
                    triples.add((nums[i], nums[left], nums[right]))
                    left += 1
                elif sum3 < 0:
                    left += 1
                else:
                    right -= 1

        return list(triples)