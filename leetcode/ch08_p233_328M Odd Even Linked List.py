'''
Given a singly linked list, group all odd nodes together followed by the even nodes. Please note here we are talking about the node number and not the value in the nodes.

You should try to do it in place. The program should run in O(1) space complexity and O(nodes) time complexity.

Example 1:

Input: 1->2->3->4->5->NULL
Output: 1->3->5->2->4->NULL
Example 2:

Input: 2->1->3->5->6->4->7->NULL
Output: 2->3->6->7->1->5->4->NULL


Constraints:

The relative order inside both the even and odd groups should remain as it was in the input.
The first node is considered odd, the second node even and so on ...
The length of the linked list is between [0, 10^4].
'''
from typing import *
class Solution:
    # 내 풀이 36ms, 93%
    def oddEvenList(self, head: ListNode) -> ListNode:

        if head is None:
            return None

        first = head
        second = head.next
        second_head = head.next

        while second and second.next:
            first.next = first.next.next
            first = first.next
            second.next = second.next.next
            second = second.next

        first.next = second_head

        return head