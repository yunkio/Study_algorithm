'''
Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
Note:
You may assume the string contains only lowercase alphabets.

Follow up:
What if the inputs contain unicode characters? How would you adapt your solution to such case?
'''
class Solution:
    # 내 풀이 - 48ms (68%)
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)