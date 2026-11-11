from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        return self.on_prefix_hashmap(nums, k)

    def on2_brute_force(self, nums: List[int], k: int) -> int:
        fit = 0
        for left in range(len(nums)):
            current_sum = 0
            for right in range(left, len(nums)):
                current_sum += nums[right]
                if current_sum == k:
                    fit += 1
        return fit

    def on_prefix_hashmap(self, nums: List[int], k: int) -> int:
        prefix_sum_cnt = {0: 1}
        current_prefix_sum = 0
        fit = 0
        for i in range(len(nums)):
            current_prefix_sum += nums[i]
            target_rest = current_prefix_sum - k
            fit += prefix_sum_cnt.get(target_rest, 0)
            prefix_sum_cnt[current_prefix_sum] = prefix_sum_cnt.get(current_prefix_sum, 0) + 1

        return fit

