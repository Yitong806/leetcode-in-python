class Solution:
    def search(self, nums: list[int], target: int) -> bool:
        return self._search(nums, target) != -1

    def _bisearch_sorted(self, nums: list[int], left: int, right: int, target: int):
        while left <= right:
            mid: int = (left + right) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                left = mid + 1
            if nums[mid] > target:
                right = mid - 1
        return -1

    def _bisearch_unsorted(self, nums: list[int], left: int, right:int, target: int):


        if left > right:
            return -1
        mid: int = (left + right) // 2
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
                return self._bisearch_sorted(nums, left, mid - 1, target)
            else:
                # 落入右半边
                return self._bisearch_unsorted(nums, mid + 1, right, target)
        elif nums[left] > nums[mid]: # 右半边有序
            # 落入右半边
            if nums[mid] < target < nums[right]:
                return self._bisearch_sorted(nums, mid + 1, right, target)
            else: # 落入左半边
                return self._bisearch_unsorted(nums, left, mid - 1, target)
        else:
            while left < len(nums) and nums[left] == nums[mid]:
                left += 1
            return self._bisearch_unsorted(nums, left, right, target)

    def _search(self, nums: list[int], target: int) -> int:
        return self._bisearch_unsorted(nums, 0, len(nums) - 1, target)

print(Solution().search([1], 0))