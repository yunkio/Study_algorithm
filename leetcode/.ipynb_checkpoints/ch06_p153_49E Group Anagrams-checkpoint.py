'''
Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note:

All inputs will be in lowercase.
The order of your output does not matter.
'''
from typing import *
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ## 내 답안
        group_list, result = dict(), []
        for word in strs:
            new_word = "".join(sorted(list(word)))
            if new_word not in group_list:
                group_list[new_word] = len(group_list)
                result.append([word])
            else:
                result[group_list[new_word]].append(word)
        return result

        ## 모범 답안
        # anagrams = collections.defaultdict(list)
        # for word in strs:
        #     anagrams[''.join(sorted(word))].append(word)
        # return anagrams.values()