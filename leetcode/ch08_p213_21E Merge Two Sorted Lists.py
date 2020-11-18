'''
Merge two sorted linked lists and return it as a new sorted list. The new list should be made by splicing together the nodes of the first two lists.

Example 1:

Input: l1 = [1,2,4], l2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:

Input: l1 = [], l2 = []
Output: []

Example 3:

Input: l1 = [], l2 = [0]
Output: [0]

Constraints:

The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both l1 and l2 are sorted in non-decreasing order.

'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import *
from copy import copy

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # 내 풀이 - 32ms, 90%
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        mylist = []
        while l1 or l2:
            if not l2 or (l1 and l1.val <= l2.val):
                l1, mylist = self.LinkedlistToList(l1, mylist)
            else:
                l2, mylist = self.LinkedlistToList(l2, mylist)

        if len(mylist) == 0:
            return ListNode(val='')
        result = ListNode(val=mylist.pop())
        while len(mylist) > 0:
            result.val, result.next = mylist.pop(), copy(result)

        return result

    def LinkedlistToList(self, ll: ListNode, l: List) -> (List, ListNode):
        l.append(ll.val)
        ll = ll.next
        return ll, l

    # 책 풀이 - 32ms, 90%
    def mergeTwoLists2(self, l1: ListNode, l2: ListNode) -> ListNode:
        if (not l1) or (l2 and l1.val > l2.val):
            l1, l2 = l2, l1
        if l1:
            l1.next = self.mergeTwoLists2(l1.next, l2)
        return l1
