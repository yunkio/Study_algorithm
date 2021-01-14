'''
Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its zigzag level order traversal as:
[
  [3],
  [20,9],
  [15,7]
]
'''
# Definition for a binary tree node.
from typing import *
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # 내 풀이 - 16ms (99.9%)
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return None

        nodes = [root]
        node_vals = [root.val]
        res = []
        new_nodes = []
        level = 0

        while True:
            if level % 2 == 0:
                res.append(node_vals)
            else:
                res.append(node_vals[::-1])
            node_vals = []

            for node in nodes:
                if node.left:
                    new_nodes.append(node.left)
                    node_vals.append(node.left.val)
                if node.right:
                    new_nodes.append(node.right)
                    node_vals.append(node.right.val)

            if new_nodes == []:
                break

            nodes, new_nodes = new_nodes, []
            level += 1

        return res