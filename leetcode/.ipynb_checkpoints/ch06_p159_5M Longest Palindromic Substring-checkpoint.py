'''
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"
'''

from typing import *
class Solution:
    def longestPalindrome(self, s: str) -> str:
    ## 내 답안
    maxlen = 0
    if len(s) <= 1:
        return s

    for i in range(len(s) - 1):
        window = 0
        while i - window >= 0 and i + window + 1 <= len(s):
            if s[i - window] == s[i + window]:
                if window * 2 + 1 > maxlen:
                    maxlen = window * 2 + 1
                    answer = s[i - window: i + window + 1]
                window += 1
            else:
                break

        if s[i] == s[i + 1]:
            window = 0
            while i - window >= 0 and i + window + 2 <= len(s):
                if s[i - window] == s[i + window + 1]:
                    if window * 2 + 2 > maxlen:
                        maxlen = window * 2 + 2
                        answer = s[i - window: i + window + 2]
                    window += 1
                else:
                    break
    ## 모범 답안
        # def expand(left: int, right: int) -> str:
        #     while left >= 0 and right <= len(s) and s[left] == s[right - 1]:
        #         left -= 1
        #         right += 1
        #     return s[left + 1:right - 1]
        #

        # if len(s) < 2 or s == s[::-1]:
        #     return s
        #
        # result = ''
        #
        # for i in range(len(s) - 1):
        #     result = max(result,
        #                  expand(i, i + 1),
        #                  expand(i, i + 2),
        #                  key=len)
        # return result
        # 훨씬 빠르고 깔끔하다!