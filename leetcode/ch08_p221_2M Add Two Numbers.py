'''
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.



Example 1:


Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]
Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]


Constraints:

The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.
'''
from typing import *
from copy import copy


class Solution:
    # 내 풀이 : 96ms, 6%
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        a, b, result = '', '', None
        while l1:
            a = str(l1.val) + a
            l1 = l1.next
        while l2:
            b = str(l2.val) + b
            l2 = l2.next

        c = list(str(int(a) + int(b)))[::-1]
        while c:
            if result is None:
                result = ListNode(val=c.pop())
            else:
                result.next, result.val = copy(result), c.pop()

        return result


