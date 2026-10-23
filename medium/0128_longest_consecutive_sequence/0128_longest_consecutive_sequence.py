class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        return self.on_hashset(nums)

    def onlogn_sort(self, nums: list[int]) -> int:
        nums.sort()
        current_value = -1000000000000
        current_cumulative = 0
        current_longest_consecutive = 0
        for n in nums:
            if current_value == -1000000000000:
                current_value = n
                current_longest_consecutive = 1
                current_cumulative = 1
                continue
            if n == current_value:
                continue
            if n == current_value + 1:
                current_cumulative += 1
                current_longest_consecutive = max(current_longest_consecutive, current_cumulative)
                current_value = n
                continue

            current_cumulative = 1
            current_value = n

        return current_longest_consecutive

    def on_hashset(self, nums: list[int]) -> int:
        deduplicated = set(nums)
        current_longest_consecutive = 0
        for n in deduplicated:
            if (n - 1) in deduplicated:
                continue
            v = n
            current_consecutive = 0
            while (v+current_consecutive) in deduplicated:
                current_consecutive += 1
            current_longest_consecutive = max(current_longest_consecutive, current_consecutive)

        return current_longest_consecutive
