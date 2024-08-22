# https://leetcode.com/problems/reverse-linked-list/description/
from typing import Optional


# Definition for singly-linked list.
"""
Given the head of a singly linked list, reverse the list, and return the reversed list.

Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Input: head = [1,2]
Output: [2,1]

"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList_1(self, head: Optional[ListNode]) -> Optional[ListNode]:
        reverse = None
        current = head
        while current:
            temp = current.next
            current.next = reverse
            reverse = current
            current = temp

        return reverse
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if (not head) or (not head.next):
            return head

        p = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return p


