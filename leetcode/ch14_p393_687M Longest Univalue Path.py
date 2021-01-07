'''
Given the root of a binary tree, return the length of the longest path, where each node in the path has the same value. This path may or may not pass through the root.

The length of the path between two nodes is represented by the number of edges between them.



Example 1:


Input: root = [5,4,5,1,1,5]
Output: 2
Example 2:


Input: root = [1,4,5,4,4,5]
Output: 2


Constraints:

The number of nodes in the tree is in the range [0, 104].
-1000 <= Node.val <= 1000
The depth of the tree will not exceed 1000.
'''
from typing import *
class Solution:
    # 내 풀이 - 404ms (43%)
    def longestUnivaluePath(self, root: TreeNode) -> int:
        self.longest = 0
        self.dfs(root)
        return self.longest

    def dfs(self, node):
        if node is None:
            return 0
        left = self.dfs(node.left)
        right = self.dfs(node.right)

        left = left + 1 if node.left and node.left.val == node.val else 0
        right = right + 1 if node.right and node.right.val == node.val else 0

        self.longest = max(self.longest, left + right)
        return max(left, right)
