#https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/
import math


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional

"""

You are given the head of a linked list. Delete the middle node, and return the head of the modified linked list.

The middle node of a linked list of size n is the ⌊n / 2⌋th node from the start using 0-based indexing, where ⌊x⌋ denotes the largest integer less than or equal to x.

For n = 1, 2, 3, 4, and 5, the middle nodes are 0, 1, 1, 2, and 2, respectively.
n / 2 결과값에서 내림 처리. 

Input: head = [1,3,4,7,1,2,6]
Output: [1,3,4,1,2,6]
Explanation:
The above figure represents the given linked list. The indices of the nodes are written below.
Since n = 7, node 3 with value 7 is the middle node, which is marked in red.
We return the new list after removing this node. 

Input: head = [1,2,3,4]
Output: [1,2,4]
Explanation:
The above figure represents the given linked list.
For n = 4, node 2 with value 3 is the middle node, which is marked in red.

Constraints:

The number of nodes in the list is in the range [1, 105].
1 <= Node.val <= 105
"""

class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        count = 0
        cur = head
        while cur:
            count += 1
            cur = cur.next

        middle_index = math.floor(count / 2)
        cur = head
        while middle_index > 0:


    def custom_print(self):
        count = 7
        middle_index = math.floor(count / 2)
        print(f"middle_index : {middle_index}")

def test_deleteMiddle():
    solution = Solution()
    solution.custom_print()

