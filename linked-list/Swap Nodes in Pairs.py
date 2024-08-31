#https://leetcode.com/problems/swap-nodes-in-pairs/description/
# Definition for singly-linked list.
from typing import Optional


"""
Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)
Input: head = [1,2,3,4]
Output: [2,1,4,3]

Input: head = []
Output: []

Input: head = [1]
Output: [1]

Constraints:

The number of nodes in the list is in the range [0, 100].
0 <= Node.val <= 100
index 0<->1, 2 <-> 3, 4 <->5 swap
1 0 2 3
1 -> 0-> 2
"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs_1(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        while cur is not None and cur.next is not None:
            temp = cur.next.next
            cur.next.next = cur
            cur.next = temp
            cur = temp
            print(f"cur value : {cur.val}")
        return head

    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        first_node = head
        second_node = head.next

        first_node.next = self.swapPairs(second_node.next)
        second_node.next = first_node
        return second_node

def test_swapPairs():
    solution = Solution()
    solution.swapPairs(ListNode(1, ListNode(2, ListNode(3, ListNode(4, None)))))
