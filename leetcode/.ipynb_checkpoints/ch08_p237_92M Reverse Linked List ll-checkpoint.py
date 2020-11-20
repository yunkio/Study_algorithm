'''
Reverse a linked list from position m to n. Do it in one-pass.

Note: 1 ≤ m ≤ n ≤ length of list.

Example:

Input: 1->2->3->4->5->NULL, m = 2, n = 4
Output: 1->4->3->2->5->NULL
'''
from typing import *
from copy import copy

class Solution:
    # 내 풀이 (24ms, 95%) - 다시 풀자.. 야매다..
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        mylist, result = [], None

        while head:
            mylist.append(head.val)
            head = head.next

        mylist = mylist[:m - 1] + mylist[m - 1:n][::-1] + mylist[n:]

        while mylist:
            if result is None:
                result = ListNode(val=mylist.pop())
            else:
                result.next, result.val = copy(result), mylist.pop()

        return result