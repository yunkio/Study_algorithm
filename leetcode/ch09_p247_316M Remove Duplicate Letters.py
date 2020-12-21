'''
Given a string s, remove duplicate letters so that every letter appears once and only once. You must make sure your result is the smallest in lexicographical order among all possible results.

Note: This question is the same as 1081: https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/

Example 1:

Input: s = "bcabc"
Output: "abc"
Example 2:

Input: s = "cbacdcbc"
Output: "acdb"

Constraints:

1 <= s.length <= 104
s consists of lowercase English letters.
'''
from typing import *
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        last_idx = {c:i for i, c in enumerate(s)}
        answer = []
        seen = set()
        for i, c in enumerate(s):
            if c not in seen:
                while answer and c < answer[-1] and i < last_idx[answer[-1]]:
                    tail = answer.pop()
                    seen.remove(tail)
                answer.append(c)
                seen.add(c)
        return ''.join(answer)