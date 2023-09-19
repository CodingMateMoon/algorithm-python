import math
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = middle = head

        while node and node.next and middle.next:  # == while node != None:
            middle = middle.next
            node = node.next.next

        return middle
        # middle = end = head
        # while end != None and middle != None:
        #     print(f"end : {end}")
        #     print(f"middle : {middle}")
        #     middle = middle.next
        #     end = end.next.next

        # return middle



def create_linked_list(values):
    if not values:
        return None

    head = ListNode(values[0])
    current = head

    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next

    return head

# Creating a linked list with values [1, 2, 3, 4, 5, 6]


if __name__ == '__main__':
    linked_list_head = create_linked_list([1, 2, 3, 4, 5, 6])




