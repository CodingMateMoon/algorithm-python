# https://leetcode.com/explore/interview/card/leetcodes-interview-crash-course-data-structures-and-algorithms/704/linked-lists/4660/
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
"""
Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.

Input: head = [1,2,3,4,5]
Output: [3,4,5]
Explanation: The middle node of the list is node 3.

Input: head = [1,2,3,4,5,6]
Output: [4,5,6]
Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.

Constraints:

The number of nodes in the list is in the range [1, 100].
1 <= Node.val <= 100
"""
from typing import Optional


class Solution:
    def middleNode_1(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current_node = head
        length = 0
        while current_node is not None:
            current_node = current_node.next
            length += 1
        #print(f"length : {length}")
        current_node = head
        for i in range(0, length // 2):
            current_node = current_node.next
            #print(f"i : {i}")
        return current_node
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """"
        arr[-1] : array의 가장 마지막 요소 가져오기
        """
        arr = [head]
        while arr[-1].next:
            arr.append(arr[-1].next)
        return arr[len(arr) // 2]

def test_middleNode():
    solution = Solution()
    solution.middleNode(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, None))))))


