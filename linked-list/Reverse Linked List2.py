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
7->/ 9->2->10->1->/ 8->6
7 <-9<-2<-10<-1 8->6
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

    def reverseBetween_2(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head:
            return None

        left_h, right_h = head, head
        stop = False

        def recurseAndReverse(right, m, n):
            nonlocal left_h, stop

            if n == 1:
                return
            right = right.next

            if m > 1:
                left_h = left_h.next
            recurseAndReverse(right, m - 1, n - 1)

            if left_h == right or right.next == left_h:
                stop = True

            if not stop:
                left_h.val, right.val = right.val, left_h.val
                left_h = left_h.next

        recurseAndReverse(right_h, left, right)
        return head
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        """
        A->B->C / C->B->A
        2 pointer: prev , cur
        prev = None
        cur = head

        third = cur.next
        cur.next = prev
        prev = cur
        cur = third

        left ~ right
        cur

        left ~ right 특정 구간만 reverse
        7->9(con)/->2->10->1->8/->6
        7->9-> /2(tail)<-10<-1<-8(prev)/ 6
        con.next = prev
        tail.next = cur

        7->9(con)->/8(prev)->1->10->2(tail)->6




        7 <- 9
        con <- tail

        7 -> 9(con) -> 2(tail) <- 10 (prev)

        """
        if not head:
            return None

        cur, prev = head, None
        while left > 1:
            prev = cur
            cur = cur.next
            left = left - 1




            
def test_reverseBetween():
    solution = Solution()
    solution.reverseBetween(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, None))))), 2, 4)



