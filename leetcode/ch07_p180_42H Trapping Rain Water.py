'''
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.


The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped. Thanks Marcos for contributing this image!

Example:

Input: [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
'''
class Solution:
    def trap(self, height: List[int]) -> int:
    # 내 답안 - 68ms, 17% 느리다..
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

    # 모범 답안 - 투포인터 56ms, 45%
    #     if not height:
    #         return 0
    #
    #     volume = 0
    #     left, right = 0, len(height) - 1
    #     left_max, right_max = height[left], height[right]
    #
    #     while left < right:
    #         left_max, right_max = max(height[left], left_max), max(height[right], right_max)
    #         # 더 높은 쪽을 향해 투 포인터 이동
    #         if left_max <= right_max:
    #             volume += left_max - height[left]
    #             left += 1
    #         else:
    #             volume += right_max - height[right]
    #             right -= 1
    #
    #     return volume
    
    # 모범 답안 - 스택 쌓기 52ms, 67%
    #     stack = []
    #     volume = 0
    #
    #     for i in range(len(height)) :
    #         # 변곡점을 만나는 경우
    #         while stack and height[i] > height[stack[-1]]:
    #             # 스택에서 꺼낸다
    #             top = stack.pop()
    #
    #             if not len(stack):
    #                 break
    #
    #             # 이전과의 차이만큼 물 높이 처리
    #             distance = i - stack[-1] - 1
    #             waters = min(height[i], height[stack[-1]]) - height[top]
    #
    #             volume += distance * waters
    #
    #         stack.append(i)
    #     return volume