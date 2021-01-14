'''
Given an array where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example:

Given the sorted array: [-10,-3,0,5,9],

One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:

      0
     / \
   -3   9
   /   /
 -10  5
'''
from typing import *
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    # 내 풀이 - 72ms (67%)
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None
        middle = len(nums) // 2
        return TreeNode(nums[middle], self.sortedArrayToBST(nums[:middle]), self.sortedArrayToBST(nums[middle+1:]))