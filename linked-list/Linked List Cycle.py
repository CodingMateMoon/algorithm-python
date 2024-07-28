#https://leetcode.com/problems/linked-list-cycle/
# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle_1(self, head: Optional[ListNode]) -> bool:
        node_info = set()
        current_node = head
        while current_node is not None:
            if current_node in node_info:
                return True
            node_info.add(current_node)
            current_node = current_node.next
        return False

    # slow pointer and fast pointer
    """
    case 1 : no cycle
    fast pointer가 먼저 끝에 도달하고 list의 길이만큼 수행시간 소요 O(n)
    
    case 2 : cycle
    fast pointer는 2 step, slow는 1 step이므로 전체 length N + cycle 길이 K만큼 시간 소요 O(N+K)
    """
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False
        slow = head
        fast = head.next
        while slow != fast:
            if fast is None or fast.next is None:
                return False
            slow = slow.next
            fast = fast.next.next
        return True
            



"""
3 -> 2 -> 0 -> -4
   -4->2
Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed)

1->2
2->1 
Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.

Constraints:

The number of the nodes in the list is in the range [0, 10^4].
-10^5 <= Node.val <= 10^5
pos is -1 or a valid index in the linked-list.
"""