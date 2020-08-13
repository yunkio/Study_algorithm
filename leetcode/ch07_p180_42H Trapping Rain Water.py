'''
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.


The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped. Thanks Marcos for contributing this image!

Example:

Input: [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
'''

    # 내 답안

class Solution:
    def trap(self, height: List[int]) -> int:

        if len(height) <= 2:
            return 0

        water = 0
        max_height, max_index, left, right = self.max_water(height)

        while left:
            max_height, max_index, left, partition = self.max_water(left)
            for i in partition:
                water += max_height - i

        while right:
            max_height, max_index, partition, right = self.max_water(right)
            for i in partition:
                water += max_height - i

        return water

    def max_water(self, height: List[int]) -> (int, int, List[int], List[int]):
        max_height = max(height)
        max_index = height.index(max(height))
        left = height[:max_index]
        right = height[max_index + 1:]
        return max_height, max_index, left, right

    # 모범 답안
