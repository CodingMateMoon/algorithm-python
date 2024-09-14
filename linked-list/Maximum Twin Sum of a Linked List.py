#https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/description/
# Definition for singly-linked list.
from typing import Optional

"""
In a linked list of size n, where n is even, the i^th node (0-indexed) of the linked list is known as the twin of the (n-1-i)^th node, if 0 <= i <= (n / 2) - 1.

For example, if n = 4, then node 0 is the twin of node 3, and node 1 is the twin of node 2. These are the only nodes with twins for n = 4.
The twin sum is defined as the sum of a node and its twin.

Given the head of a linked list with even length, return the maximum twin sum of the linked list.

Input: head = [5,4,2,1]
Output: 6
Explanation:
Nodes 0 and 1 are the twins of nodes 3 and 2, respectively. All have twin sum = 6.
There are no other nodes with twins in the linked list.
Thus, the maximum twin sum of the linked list is 6.

Ex2:
Input: head = [4,2,2,3]
Output: 7
Explanation:
The nodes with twins present in this linked list are:
- Node 0 is the twin of node 3 having a twin sum of 4 + 3 = 7.
- Node 1 is the twin of node 2 having a twin sum of 2 + 2 = 4.
Thus, the maximum twin sum of the linked list is max(7, 4) = 7. 

Constraints:

The number of nodes in the list is an even integer in the range [2, 105].
1 <= Node.val <= 105

index 합이 n-1. n=4 -> 0 + 3 = 3, 1 + 2 = 3 [n-1]
twin 노드 value 합이 가장 큰 경우 구하기
reverse 후 n/2까지 twin 합 중 가장 큰 값 저장
"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow, fast = head, head
        max_twin_sum = 0

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        prev = None

        while slow:
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp

        while prev:
            max_twin_sum = max(max_twin_sum, prev.val + head.val)
            prev = prev.next
            head = head.next

        print(f"max_twin_sum : {max_twin_sum}")

        return max_twin_sum

    def printNode(self, head: Optional[ListNode]):
        current = head
        index = 0
        while current:
            print(f"[{index}] : {current.val}")
            current = current.next


def test_pairSum():
    solution = Solution()
    solution.pairSum(ListNode(5, ListNode(4, ListNode(2, ListNode(1, None)))))

