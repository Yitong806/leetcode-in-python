class Solution:
    def bisearch_sorted(self, nums: list[int], left: int, right: int, target: int):
        while left <= right:
            mid: int = (left + right) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                left = mid + 1
            if nums[mid] > target:
                right = mid - 1
        return -1

    def bisearch_unsorted(self, nums: list[int], left: int, right:int, target: int):
        mid: int = (left + right) // 2
        if left > right:
            return -1

        if nums[mid] == target:
            return mid
        if nums[left] == target:
            return left
        if nums[right] == target:
            return right
        if nums[left] < nums[mid]:# 左半边有序
            # 观察是否落在左半边
            if nums[left] < target < nums[mid]:
                # 落入左半边
                return self.bisearch_sorted(nums, left, mid - 1, target)
            else:
                # 落入右半边
                return self.bisearch_unsorted(nums, mid + 1, right, target)
        else: # 右半边有序
            # 落入右半边
            if nums[mid] < target < nums[right]:
                return self.bisearch_sorted(nums, mid + 1, right, target)
            else: # 落入左半边
                return self.bisearch_unsorted(nums, left, mid - 1, target)

    def search(self, nums: list[int], target: int) -> int:
        return self.bisearch_unsorted(nums, 0, len(nums) - 1, target)

