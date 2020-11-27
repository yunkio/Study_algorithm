'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.


Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
Example 4:

Input: s = "([)]"
Output: false
Example 5:

Input: s = "{[]}"
Output: true


Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
'''
from typing import *
class Solution:
    # 내 풀이 - 20ms, 99%
    def isValid(self, s: str) -> bool:
        A = []
        dic = {')' : '(', ']' : '[', '}' : '{'}
        for char in s:
            if char in ['(', '[', '{']:
                A.append(char)
            elif not A or A.pop() != dic[char] :
                return False
        return not A


