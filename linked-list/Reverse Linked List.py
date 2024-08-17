# https://leetcode.com/problems/reverse-linked-list/description/
from typing import Optional


# Definition for singly-linked list.
"""
Given the head of a singly linked list, reverse the list, and return the reversed list.

"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
