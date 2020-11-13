'''
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
'''

from typing import *


class Solution:

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # 내 풀이 - 944ms, 47.8%
        result = []
        nums.sort()
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            a = nums[i]
            new_nums = nums[i + 1:]

            j = 0
            k = len(new_nums) - 1

            while k > j:
                b = new_nums[j]
                c = new_nums[k]

                if a + b + c < 0:
                    j += 1
                elif a + b + c > 0:
                    k -= 1
                else:
                    answer = [a, b, c]
                    result.append(answer)
                    while k > j and new_nums[j] == new_nums[j + 1]:
                        j += 1
                    while k > j and new_nums[k] == new_nums[k - 1]:
                        k -= 1
                    k -= 1
        return result


