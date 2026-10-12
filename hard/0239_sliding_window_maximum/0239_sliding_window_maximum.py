from collections import deque
import heapq


class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        return self.onlogn_priority_queue(nums, k)

    def onk_brute_force(self, nums: list[int], k: int) -> list[int]:
        # TLE, 38/53 testcases passed
        results = []
        for i in range(0, len(nums) - k + 1):
            maximum = -10001
            for j in range(i, i + k):
                if nums[j] > maximum:
                    maximum = nums[j]
            results.append(maximum)
        return results

    def onlogn_priority_queue(self, nums: list[int], k: int) -> list[int]:
        heap = []
        answer = []
        for i in range(len(nums)):
            heapq.heappush(heap, (-nums[i], i))

            while len(heap) > 0 and heap[0][1] <= i - k:
                heapq.heappop(heap)

            if i >= k - 1:
                answer.append(-heap[0][0])

        return answer

    def on_descending_queue(self, nums: list[int], k: int) -> list[int]:
        index_descending_queue = deque()
        answer = []
        for i in range(len(nums)):
            v = nums[i]

            while len(index_descending_queue) > 0 and nums[index_descending_queue[-1]] < v:
                index_descending_queue.pop()

            index_descending_queue.append(i)
            if index_descending_queue[0] <= i - k:
                index_descending_queue.popleft()
            if i >= k - 1:
                answer.append(nums[index_descending_queue[0]])

        return answer



