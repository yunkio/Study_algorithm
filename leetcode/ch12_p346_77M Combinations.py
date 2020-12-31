'''
77. Combinations
Medium

1902

78

Add to List

Share
Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

You may return the answer in any order.



Example 1:

Input: n = 4, k = 2
Output:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
Example 2:

Input: n = 1, k = 1
Output: [[1]]


Constraints:

1 <= n <= 20
1 <= k <= n
'''
from typing import *
class Solution:
    # 내 풀이 - 772ms (7.2%)
    def combine(self, n: int, k: int) -> List[List[int]]:
        answer = self.myfunc(k, list(range(1, n + 1)))

        return answer

    def myfunc(self, k, nums):
        if not k:
            return [[]]
        if not nums:
            return []

        head = [nums[0]]
        tail = nums[1:]
        new_comb = [head + comb for comb in self.myfunc(k - 1, tail)]

        return new_comb + self.myfunc(k, tail)