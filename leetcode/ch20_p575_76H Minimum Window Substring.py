'''
Given two strings s and t, return the minimum window in s which will contain all the characters in t. If there is no such window in s that covers all characters in t, return the empty string "".

Note that If there is such a window, it is guaranteed that there will always be only one unique minimum window in s.



Example 1:

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Example 2:

Input: s = "a", t = "a"
Output: "a"


Constraints:

1 <= s.length, t.length <= 105
s and t consist of English letters.
'''
from typing import *
from collections import Counter
class Solution:
    # 108ms (74%)
    def minWindow(self, s: str, t: str) -> str:

        need_char_set = set(t)
        need = Counter(t)
        missing = len(t)

        left = right = 0
        ans = ''
        ans_l = float("inf")

        while right < len(s):
            char = s[right]

            if char in need_char_set:
                if need[char] > 0:
                    missing -= 1
                need[char] -= 1

            while missing <= 0:
                start_char = s[left]
                if start_char in need_char_set:
                    need[start_char] += 1
                    if need[start_char] > 0:
                        missing += 1

                if (right - left) < ans_l:
                    ans = s[left:right + 1]
                    ans_l = len(ans)

                left += 1

            right += 1

        return ans