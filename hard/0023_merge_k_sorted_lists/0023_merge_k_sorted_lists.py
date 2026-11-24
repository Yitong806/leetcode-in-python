# Definition for singly-linked list.
from __future__ import annotations

import heapq


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: list[ListNode | None]) -> ListNode | None:
        return self.onlogk_heap(lists)

    @staticmethod
    def size_sum(lists: list[ListNode | None]) -> int:
        ans = 0
        for n in lists:
            curr = n
            cnt = 0
            while curr:
                curr = curr.next
                cnt += 1
            ans += cnt
        return ans

    def okn_brute_force(self, lists: list[ListNode| None]) -> ListNode | None:
        def min_node_index(lists: list[ListNode | None]) -> int:
            min_value = 15033
            for n in lists:
                if not n:
                    continue
                if n.val < min_value:
                    min_value = n.val

            for i in range(len(lists)):
                if not lists[i]:
                    continue
                if lists[i].val == min_value:
                    return i
            return -1


        head: ListNode|None = None
        current: ListNode|None = None
        size: int = Solution.size_sum(lists)
        while size > 0:
            min_index = min_node_index(lists)
            if head is None:
                head = lists[min_index]
                current = lists[min_index]
            else:
                current.next = lists[min_index]
                current = current.next
            lists[min_index] = lists[min_index].next
            size -= 1

        return head

    def onlogk_heap(self, lists: list[ListNode|None]) -> ListNode|None:
        heap = []
        for i in range(len(lists)):
            n = lists[i]
            if n:
                heapq.heappush(heap, (n.val, i, n))

        head = None
        curr = None
        while heap:
            pop_val, i, pop = heapq.heappop(heap)
            if not head:
                head = pop
                curr = pop
            else:
                curr.next = pop
                curr = pop
            if pop.next:
                heapq.heappush(heap,(pop.next.val, i, pop.next))

        return head
