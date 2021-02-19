'''
Given a string s that consists of only uppercase English letters, you can perform at most k operations on that string.

In one operation, you can choose any character of the string and change it to any other uppercase English character.

Find the length of the longest sub-string containing all repeating letters you can get after performing the above operations.

Note:
Both the string's length and k will not exceed 104.

Example 1:

Input:
s = "ABAB", k = 2

Output:
4

Explanation:
Replace the two 'A's with two 'B's or vice versa.


Example 2:

Input:
s = "AABABBA", k = 1

Output:
4

Explanation:
Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
'''
from typing import *
from collections import defaultdict

class Solution:
    # 104ms (86%)
    def characterReplacement(self, s: str, k: int) -> int:
        occurence_map = defaultdict(int)
        left, res, max_repeat_count = 0, 0, 0

        for right in range(len(s)):
            current = s[right]
            occurence_map[current] += 1
            max_repeat_count = max(max_repeat_count, occurence_map[current])

            if (right-left+1 - max_repeat_count) > k:
                occurence_map[s[left]] -= 1
                left += 1

            res = max(res, right-left+1)

        return res