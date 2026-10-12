from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        return self.on_descending_queue(nums, k)

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


if __name__ == '__main__':
    nums = [3,1,1,3]
    k = 3
    print(Solution().maxSlidingWindow(nums, k))


