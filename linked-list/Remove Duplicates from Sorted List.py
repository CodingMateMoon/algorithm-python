# https://leetcode.com/explore/interview/card/leetcodes-interview-crash-course-data-structures-and-algorithms/704/linked-lists/4597/
# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

"""
Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.
Input: head = [1,1,2]
Output: [1,2]
Input: head = [1,1,2,3,3]
Output: [1,2,3]
The number of nodes in the list is in the range [0, 300].
-100 <= Node.val <= 100
The list is guaranteed to be sorted in ascending order.
순회하면서 중복을 제거한 노드 인덱스 정보를 저장 후 next.next 등으로 건너뛰어서 저장. 이전 노드 정보 가지고 있기
"""
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        val_check = [head.val]
        current_node = head.next
        previous_node = head
        while current_node.next is not None:
            if current_node.val in val_check:
                previous_node.next = previous_node.next.next
                current_node = previous_node.next
                continue
            current_node = current_node.next
            previous_node = previous_node.next

        return head

