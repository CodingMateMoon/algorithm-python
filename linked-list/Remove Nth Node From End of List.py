#https://leetcode.com/problems/remove-nth-node-from-end-of-list/
# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd_1(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head.next is None:
            return None

        cur = head
        length = 0

        while cur:
            cur = cur.next
            length += 1

        cur = head
        target_index = length - n

        while target_index > 1:
            cur = cur.next
            target_index -= 1

        # length 2, n = 2인 경우
        if target_index == 0:
            return head.next

        cur.next = cur.next.next
        return head

    """
    뒤에서 n번째인 노드 제거
    length 계산. length - n 만큼 이동 후 해당 노드 제거
    length : 5, n = 2
    5 - 2 = 3 (target)
    while target > 0
        cur = cur.next
        target -= 1

    Input: head = [1,2,3,4,5], n = 2
    Output: [1,2,3,5]
    Example 2:

    Input: head = [1], n = 1
    Output: []
    Example 3:

    Input: head = [1,2], n = 1
    Output: [1]

    Input: head = [1,2], n = 2 
    Output: [2]

    Constraints:

    The number of nodes in the list is sz.
    1 <= sz <= 30
    0 <= Node.val <= 100
    1 <= n <= sz
    """

    def removeNthFromEnd_1(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        length = 0
        first = head

        while first:
            first = first.next
            length += 1

        # length - n - 1 노드.next 제거
        # e.g length 5 | 5 - 2 = 3.
        length -= n
        first = dummy
        while length > 0:
            length -= 1
            first = first.next
        first.next = first.next.next
        return dummy.next

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        first = dummy
        second = dummy

        for _ in range(n + 1):
            first = first.next

        while first:
            first = first.next
            second = second.next
        second.next = second.next.next
        return dummy.next






