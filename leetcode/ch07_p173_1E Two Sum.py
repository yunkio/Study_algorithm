'''
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
'''


from typing import *
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ## 내 답안 - 808ms, 29%.. 느려터짐
        nums = collections.deque(nums)
        i = 0
        while len(nums) > 0:
            a = nums.popleft()
            if (target - a) in nums:
                j = nums.index(target-a) + 1 + i
                return [i,j]
            i += 1

        ## 모범 답안 - 52ms 훨씬 빠르다.
        # d = {}
        # for i, num in enumerate(nums):
        #     n = target - num
        #     if n in d:
        #         return [d[n], i]
        #     else:
        #         d[num] = i

        # 훨씬 빠르다!! Dictionary를 이용해서 차를 저장해놓고 필요할 때 끄집어쓰기
