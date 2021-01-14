'''
A tree is an undirected graph in which any two vertices are connected by exactly one path. In other words, any connected graph without simple cycles is a tree.

Given a tree of n nodes labelled from 0 to n - 1, and an array of n - 1 edges where edges[i] = [ai, bi] indicates that there is an undirected edge between the two nodes ai and bi in the tree, you can choose any node of the tree as the root. When you select a node x as the root, the result tree has height h. Among all possible rooted trees, those with minimum height (i.e. min(h))  are called minimum height trees (MHTs).

Return a list of all MHTs' root labels. You can return the answer in any order.

The height of a rooted tree is the number of edges on the longest downward path between the root and a leaf.



Example 1:


Input: n = 4, edges = [[1,0],[1,2],[1,3]]
Output: [1]
Explanation: As shown, the height of the tree is 1 when the root is the node with label 1 which is the only MHT.
Example 2:


Input: n = 6, edges = [[3,0],[3,1],[3,2],[3,4],[5,4]]
Output: [3,4]
Example 3:

Input: n = 1, edges = []
Output: [0]
Example 4:

Input: n = 2, edges = [[0,1]]
Output: [0,1]


Constraints:

1 <= n <= 2 * 104
edges.length == n - 1
0 <= ai, bi < n
ai != bi
All the pairs (ai, bi) are distinct.
The given input is guaranteed to be a tree and there will be no repeated edges.
'''
from typing import *
'''
      2
     / \
    1   3
   /     \
  0       4
'''
class Solution:
    # 내 풀이 - 232ms (81%)
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        mydict = collections.defaultdict(list)
        for a, b in edges:
            mydict[a].append(b)
            mydict[b].append(a)
        # mydict - {1: [0, 2], 0: [1], 2: [1, 3], 3: [2, 4], 4: [3]}

        leaves = [leaf for leaf in range(n) if len(mydict[leaf]) == 1]
        # leaves - [0, 4]

        while leaves and len(leaves) < len(mydict):
            new = []
            for a in leaves:
                for b in mydict[a]:
                    mydict[b].remove(a)
                    if len(mydict[b]) == 1:
                        new.append(b)
                mydict.pop(a)
            leaves = new
            # leaves - [1, 3] -> [2]

        # mydict - {2: []}
        return list(mydict)