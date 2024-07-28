# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
"""
Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.

Input: head = [1,2,3,4,5]
Output: [3,4,5]
Explanation: The middle node of the list is node 3.

Constraints:

The number of nodes in the list is in the range [1, 100].
1 <= Node.val <= 100
"""
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
