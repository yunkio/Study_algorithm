'''
Given a paragraph and a list of banned words, return the most frequent word that is not in the list of banned words.  It is guaranteed there is at least one word that isn't banned, and that the answer is unique.

Words in the list of banned words are given in lowercase, and free of punctuation.  Words in the paragraph are not case sensitive.  The answer is in lowercase.

Example:

Input:
paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]
Output: "ball"
Explanation:
"hit" occurs 3 times, but it is a banned word.
"ball" occurs twice (and no other word does), so it is the most frequent non-banned word in the paragraph.
Note that words in the paragraph are not case sensitive,
that punctuation is ignored (even if adjacent to words, such as "ball,"),
and that "hit" isn't the answer even though it occurs more because it is banned.
'''

from typing import *
import re

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
    ## 내 답안
        paragraph = re.sub('[^a-z0-9 ]', ' ', paragraph.lower()).split()
        not_banned = [word for word in paragraph if word not in banned]
        return collections.Counter(not_banned).most_common(n=1)[0][0]

    ## 모범 답안
        # words = [word for word in re.sub(r'[^\w]', ' ', paragraph)
        #          .lower().split()
        #                 if word not in banned]
        # counts = collections.Counter(words)
        # return counts.most_common(1)[0][0]
        # 거의 유사하다..