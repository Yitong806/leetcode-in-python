from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        return self.o1_space(headA, headB)

    def o1_space(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        p1, p2 = headA, headB
        while p1 is not p2:
            p1 = p1.next if p1 is not None else headB
            p2 = p2.next if p2 is not None else headA
        return p1

    def on_space(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        s1 = set()
        p1 = headA
        while p1 is not None:
            s1.add(p1)
            p1 = p1.next

        p2 = headB
        while p2 is not None:
            if p2 in s1:
                return p2
            p2 = p2.next

        return None