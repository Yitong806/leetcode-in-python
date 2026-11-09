from __future__ import annotations


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self) -> str:
        return str(self.val)


class Solution:
    def reverseKGroup(self, head: ListNode | None, k: int) -> ListNode | None:
        current = head
        head_tails = []
        while current is not None:
            sub_head = current
            sub_tail = self.jump_k(sub_head, k)
            head_tails.append((sub_head, sub_tail))
            if not sub_tail:
                break
            current = sub_tail.next

        for h, t in head_tails:
            self.reverse(h, t)

        if len(head_tails) == 1:
            return head_tails[0][1] if head_tails[0][1] else head

        head_tails[0][0].next = None
        for i in range(len(head_tails) - 1):
            new_tail_this = head_tails[i][0]
            new_head_next = head_tails[i + 1][1]
            new_tail_this.next = new_head_next

        head_tails[-2][0].next = head_tails[-1][1] if head_tails[-1][1] else head_tails[-1][0]

        return head_tails[0][1]

    def jump_k(self, head: ListNode| None, k: int):
        temp = head
        i = 0
        while i < k - 1 and temp is not None:
            temp = temp.next
            i += 1
        return temp

    def reverse(self, head: ListNode|None, tail: ListNode|None):
        if not tail:
            return
        prev = None
        curr = head
        while True:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
            if prev is tail:
                break
