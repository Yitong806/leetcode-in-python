import heapq


class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        return self.onlogk_heap(nums, k)

    def onlogn_sort(self, nums: list[int], k: int) -> int:
        nums.sort(reverse=True)
        return nums[k - 1]

    def onlogk_heap(self, nums: list[int], k: int) -> int:
        heap = []
        for n in nums:
            if len(heap) < k:
                heap.append(n)
                if len(heap) == k:
                    heapq.heapify(heap)
                continue
            pop = heapq.heappop(heap)
            heapq.heappush(heap, max(n, pop))

        return heapq.heappop(heap)