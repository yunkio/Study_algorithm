'''
Given an integer array nums, return all possible subsets (the power set).

The solution set must not contain duplicate subsets.



Example 1:

Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
Example 2:

Input: nums = [0]
Output: [[],[0]]


Constraints:

1 <= nums.length <= 10
-10 <= nums[i] <= 10
All the numbers of nums are unique.
'''
from typing import *
class Solution:
    # 내 풀이 - 32ms (79.51%)
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.answer = []
        for n in range(len(nums) + 1):
            self.answer += self.myfunc(n, nums)
        return self.answer

    def myfunc(self, k, nums):
        if not k:
            return [[]]
        if not nums:
            return []

        head = [nums[0]]
        tail = nums[1:]
        new_comb = [head + comb for comb in self.myfunc(k - 1, tail)]

        return new_comb + self.myfunc(k, tail)