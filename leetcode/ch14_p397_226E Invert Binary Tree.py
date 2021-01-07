'''
Invert a binary tree.

Example:

Input:

     4
   /   \
  2     7
 / \   / \
1   3 6   9
Output:

     4
   /   \
  7     2
 / \   / \
9   6 3   1
Trivia:
This problem was inspired by this original tweet by Max Howell:

Google: 90% of our engineers use the software you wrote (Homebrew), but you can’t invert a binary tree on a whiteboard so f*** off.
'''
from typing import *
class Solution:
    # 내 풀이 : 28ms (83%)
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        return TreeNode(root.val, self.invertTree(root.right), self.invertTree(root.left))