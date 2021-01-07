'''
There are N network nodes, labelled 1 to N.

Given times, a list of travel times as directed edges times[i] = (u, v, w), where u is the source node, v is the target node, and w is the time it takes for a signal to travel from source to target.

Now, we send a signal from a certain node K. How long will it take for all nodes to receive the signal? If it is impossible, return -1.



Example 1:



Input: times = [[2,1,1],[2,3,1],[3,4,1]], N = 4, K = 2
Output: 2


Note:

N will be in the range [1, 100].
K will be in the range [1, N].
The length of times will be in the range [1, 6000].
All edges times[i] = (u, v, w) will have 1 <= u, v <= N and 0 <= w <= 100.
'''
from typing import *


class Solution:
    # 내 풀이 - 1880ms (6%)
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        matrix = [[float("inf") for _ in range(N)] for _ in range(N)]

        for i in range(N):
            matrix[i][i] = 0
        for node in times:
            matrix[node[0] - 1][node[1] - 1] = node[2]
        for k in range(N):
            for i in range(N):
                for j in range(N):
                    matrix[i][j] = min(matrix[i][j], matrix[i][k] + matrix[k][j])

        if max(matrix[K - 1]) == float("inf"):
            return -1
        else:
            return max(matrix[K - 1])