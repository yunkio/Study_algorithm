'''
Given a singly linked list, determine if it is a palindrome.

Example 1:

Input: 1->2
Output: false
Example 2:

Input: 1->2->2->1
Output: true
Follow up:
Could you do it in O(n) time and O(1) space?
'''
from typing import *
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # 내 풀이 64ms - 90%
    def isPalindrome(self, head: ListNode) -> bool:
        if head is None:
            return True
        mylist = []
        length = 0

        while head is not None:
            mylist.append(head.val)
            head = head.next
            length += 1

        for i in range(length // 2):
            if mylist[i] != mylist[length - 1 - i]:
                return False

        return True

    # 모범 풀이 (러너) - 68ms, 76%
    def isPalindrome2(self, head: ListNode) -> bool:
        rev = None
        slow = fast = head

        while fast and fast.next:
            fast = fast.next.next
            rev, rev.next, slow = slow, rev, slow.next
        if fast:
            slow = slow.next

        while rev and rev.val == slow.val:
            slow, rev = slow.next, rev.next

        return not rev