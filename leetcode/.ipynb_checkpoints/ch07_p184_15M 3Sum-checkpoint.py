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
        # 내 풀이 - 아 시간초과 뜸
        result = []
        nums.sort()

        for i in range(len(nums)):
            a = nums[i]
            new_nums = nums[i + 1:]
            print(new_nums)
            if len(new_nums) >= 2:
                j = 0
                k = len(new_nums) - 1

                while k > j:
                    b = new_nums[k]
                    c = new_nums[j]
                    if a + b + c == 0:
                        answer = [a, b, c]
                        result.append(answer)
                    elif a + b + c < 0:
                        j -= 1
                    else:
                        k += 1
        return result

#####################################################################################

