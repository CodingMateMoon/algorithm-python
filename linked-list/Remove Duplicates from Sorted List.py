# https://leetcode.com/explore/interview/card/leetcodes-interview-crash-course-data-structures-and-algorithms/704/linked-lists/4597/
# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

"""
Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.
"""
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]: