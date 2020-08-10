from typing import *

class Solution:
    def isPalindrome(self, s: str) -> bool:

        ## 내 풀이
        strs = ''
        for char in s:
            if char.isalnum():
                strs += char.lower()
        for i in range(len(strs)//2):
            if strs[i] != strs[-(i+1)]:
                return False
        return True

        ## 최적화 풀이
        # s = re.sub('[^a-z0-9]', '', s.lower())
        # return s == s[::-1]