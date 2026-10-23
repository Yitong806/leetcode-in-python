import heapq
from collections import Counter


class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        return self.onlogk_hash_heap(nums, k)

    def onlogn_hash_sort(self, nums: list[int], k: int) -> list[int]:
        freq = Counter(nums)
        items = sorted(freq.items(), key=lambda v: v[1], reverse=True)
        return [items[i][0] for i in range(k)]

    def onlogk_hash_heap(self, nums: list[int], k: int) -> list[int]:
        freq = Counter(nums)
        hp = []
        for key, count in freq.items():
            if len(hp) < k:
                hp.append((count, key))
                if len(hp) == k:
                    heapq.heapify(hp)
                continue

            min_freq, min_key = hp[0]
            if min_freq < count:
                heapq.heappop(hp)
                heapq.heappush(hp,(count, key))

        return [item[1] for item in hp]

