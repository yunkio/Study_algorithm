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

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
    # 내 풀이
        nums.sort()
        left, middle, right = 0, 1, len(nums) - 1
        answer = []

        while right > left:
            while right > middle:
                result = nums[left] + nums[middle] + nums[right]
                if result > 0:
                    break
                elif result == 0:
                    answer.append([nums[left], nums[middle], nums[right]])
                else:
                    middle += 1
            if nums[left] + nums[right] > 0:
                right -= 1
            else:
                left += 1
                middle = left + 1
        return answer