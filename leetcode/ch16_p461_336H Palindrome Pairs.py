'''
Given a list of unique words, return all the pairs of the distinct indices (i, j) in the given list, so that the concatenation of the two words words[i] + words[j] is a palindrome.



Example 1:

Input: words = ["abcd","dcba","lls","s","sssll"]
Output: [[0,1],[1,0],[3,2],[2,4]]
Explanation: The palindromes are ["dcbaabcd","abcddcba","slls","llssssll"]
Example 2:

Input: words = ["bat","tab","cat"]
Output: [[0,1],[1,0]]
Explanation: The palindromes are ["battab","tabbat"]
Example 3:

Input: words = ["a",""]
Output: [[0,1],[1,0]]


Constraints:

1 <= words.length <= 5000
0 <= words[i].length <= 300
words[i] consists of lower-case English letters.
'''
from typing import *
class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        # 내 풀이 - 468ms (80%)
        mydict = {word: index for index, word in enumerate(words)}
        ans = []

        for index, word in enumerate(words):
            for i in range(len(word) + 1):
                left = word[:i]
                right = word[i:]

                # left가 palindrome이고, right의 reverse가 단어로 존재하면,
                # right[::-1] + left + right = right[::-1] + word 는 palindrome
                # 반대로 right가 palindrome이고, left의 reverse가 단어로 존재하면,
                # left + right + left[::-1] = word + left[::-1] 이 palindrome

                if (left == left[::-1]) and (right[::-1] in mydict) and (mydict[right[::-1]] != index):
                    ans.append((mydict[right[::-1]], index))

                if (right == right[::-1]) and (left[::-1] in mydict) and (mydict[left[::-1]] != index):
                    ans.append((index, mydict[left[::-1]]))

        return list(set(ans))