'''
Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.

Clarification: The input/output format is the same as how LeetCode serializes a binary tree. You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.



Example 1:


Input: root = [1,2,3,null,null,4,5]
Output: [1,2,3,null,null,4,5]
Example 2:

Input: root = []
Output: []
Example 3:

Input: root = [1]
Output: [1]
Example 4:

Input: root = [1,2]
Output: [1,2]


Constraints:

The number of nodes in the tree is in the range [0, 104].
-1000 <= Node.val <= 1000
'''
from typing import *

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:
# 내 풀이 - 152ms (42%)
    def serialize(self, root):

        def dfs(root, string=''):
            if not root:
                return 'None'
            string += str(root.val)
            string += ',' + dfs(root.left)
            string += ',' + dfs(root.right)
            return string

        return dfs(root)

        # 1,2,None,None,3,4,None,None,5,None,None

    def deserialize(self, data):

        def dfs(string):
            if string[0] == "None":
                string.pop(0)
                return None
            root = TreeNode(string.pop(0))
            root.left = dfs(string)
            root.right = dfs(string)
            return root

        return dfs(data.split(","))

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))