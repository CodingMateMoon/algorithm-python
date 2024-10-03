#https://leetcode.com/explore/interview/card/leetcodes-interview-crash-course-data-structures-and-algorithms/704/linked-lists/4598/
# Definition for singly-linked list.
from typing import Optional

"""
Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list from position left to position right, and return the reversed list.
Example 2:
Input: head = [1,2,3,4,5], left = 2, right = 4
Output: [1,4,3,2,5]

left side, reverse side, right side 연결
1 -> (4, 3, 2) -> 5

Example 2:

Input: head = [5], left = 1, right = 1
Output: [5]

Constraints:

The number of nodes in the list is n.
1 <= n <= 500
-500 <= Node.val <= 500
1 <= left <= right <= n

left ~ right 특정 구간만 reverse
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseBetween_1(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        current = head
        before = None
        index = 0
        while current:
            index += 1
            if left <= index <= right:
                temp = current.next
                current.next = before
                before = current
                current = temp

                continue
            current = current.next
        self.printNode(head)

    def printNode(self, head:Optional[ListNode]):
        current = head
        index = 1
        while current:
            print(f"[{index}] : {current.val}")
            index += 1
            current = current.next

    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head:
            return None

        left, right = head, head
        stop = False

        def recurseAndReverse(right, m, n):
            nonlocal left, stop

            if n == 1:
                return
            right = right.next

            if m > 1:
                left = left.next
            recurseAndReverse(right, m - 1, n - 1)

            if left == right or right.next == left:
                stop = True

            if not stop:
                left.val, right.val = right.val, left.val



            
def test_reverseBetween():
    solution = Solution()
    solution.reverseBetween(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, None))))), 2, 4)



