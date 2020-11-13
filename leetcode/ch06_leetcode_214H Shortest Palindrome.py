'''
214. Shortest Palindrome
Hard

1370

138

Add to List

Share
Given a string s, you can convert it to a palindrome by adding characters in front of it. Find and return the shortest palindrome you can find by performing this transformation.



Example 1:

Input: s = "aacecaaa"
Output: "aaacecaaa"
Example 2:

Input: s = "abcd"
Output: "dcbabcd"


Constraints:

0 <= s.length <= 5 * 104
s consists of lowercase English letters only.
'''

class Solution:
    # 내 풀이 - 1088ms, 5% 어케 풀긴 풀었다
    def shortestPalindrome(self, s: str) -> str:
        answer = ''
        if s == s[::-1]:
            return s
        for i in range(len(s)):
            a, b = s[:i], s[i:]
            if len(a) > 0 and a[::-1] == b[:len(a)]:
                answer = b[::-1] + b
            elif a[::-1] == b[1:len(a)+1]:
                answer = b[::-1] + b[1:]
        return answer