import math


class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        nums.sort()
        index_left, index_right = math.floor(len(nums)/2), math.floor(len(nums) / 2)

        median_left, median_right = nums[index_left], nums[index_right]
        av = sum(nums) / len(nums)
        av_left, av_right = math.floor(av), math.ceil(av)

        return min(sum(abs(x - av_left) for x in nums), sum(abs(x - av_right) for x in nums),
                   sum(abs(x - median_left) for x in nums), sum(abs(x - median_right) for x in nums)
                   )