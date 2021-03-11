'''
Given a string s and an integer k, return the length of the longest substring of s such that the frequency of each character in this substring is greater than or equal to k.



Example 1:

Input: s = "aaabb", k = 3
Output: 3
Explanation: The longest substring is "aaa", as 'a' is repeated 3 times.
Example 2:

Input: s = "ababbc", k = 2
Output: 5
Explanation: The longest substring is "ababb", as 'a' is repeated 2 times and 'b' is repeated 3 times.


Constraints:

1 <= s.length <= 104
s consists of only lowercase English letters.
1 <= k <= 105
'''
from typing import *
from collections import Counter

from collections import Counter


class Solution:
    # 내 풀이 - 20ms (99.9%)
    def longestSubstring(self, s: str, k: int) -> int:
        count = Counter(s)

        left, right = 0, 0
        n = len(s)

        while right < n:
            char = s[right]

            if count[char] >= k:
                right += 1

            else:
                if right - left >= k:
                    return max(self.longestSubstring(s[left:right], k), self.longestSubstring(s[right:], k))
                right += 1
                left = right

        if right - left < k:
            return 0

        return right - left