'''
Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Example:

Input:  [1,2,3,4]
Output: [24,12,8,6]
Constraint: It's guaranteed that the product of the elements of any prefix or suffix of the array (including the whole array) fits in a 32 bit integer.

Note: Please solve it without division and in O(n).

Follow up:
Could you solve it with constant space complexity? (The output array does not count as extra space for the purpose of space complexity analysis.)

'''
from typing import *
class Solution:
    # 내 풀이 - 228ms, 49% 느려
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        A,B = [1], []
        a,b = 1,1
        for i in range(len(nums)):
            a *= nums[i]
            b *= nums[-(i+1)]
            A.append(a)
            B.append(b)
        B = B[::-1]
        B.append(1)
        return [A[i] * B[i+1] for i in range(len(nums))]