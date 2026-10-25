# Definition for singly-linked list.
from __future__ import annotations


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def jump_n_nodes(self, start: ListNode, n: int):
        for _ in range(n):
            start = start.next

        return start

    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        if head is None:
            return None
        fast = self.jump_n_nodes(head, n)
        slow = head
        target, target_prev = None, None
        while fast is not None:
            if fast.next is None:
                target_prev = slow
            fast = fast.next
            slow = slow.next

        target = slow
        if target is head:
            return head.next

        target_prev.next = target.next
        return head




