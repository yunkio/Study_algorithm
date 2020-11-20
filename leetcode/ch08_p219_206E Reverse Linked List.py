  '''
Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
Follow up:

A linked list can be reversed either iteratively or recursively. Could you implement both?

'''
from typing import *
from copy import copy
from collections import deque

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # 내 풀이 (막장) - 40ms, 26.21%
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return head
        mylist = deque()
        result = None
        while head:
            mylist.append(head.val)
            head = head.next
        while mylist:
            if result is None:
                result = ListNode(val=mylist.popleft())
                continue
            result.val, result.next = mylist.popleft(), copy(result)
        return result

    def reverseList2(self, head: ListNode) -> ListNode:
    # 책 풀이 (1) 재귀 - 40ms, 26.21%
        def reverse(head: ListNode, result: ListNode = None) -> ListNode:
            if not head:
                return result
            new, head.next = head.next, result
            return reverse(new, head)
        return reverse(head)

    def reverseList3(self, head: ListNode) -> ListNode:
    # 책 풀이 (2) 반복 - 32ms, 85.51%
        node, prev = head, None
        while node:
            next, node.next = node.next, prev
            prev, node = node, next
        return prev

