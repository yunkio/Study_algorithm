'''
Given an m x n 2d grid map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.



Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3


Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 300
grid[i][j] is '0' or '1'.
'''
from typing import *
class Solution:
    # 내 풀이 - 140ms, 64%
    def numIslands(self, grid: List[List[str]]) -> int:
        self.grid, self.m, self.n, self.answer = grid, len(grid), len(grid[0]), 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    self.findland(i, j)
                    self.answer += 1
        return self.answer

    def findland(self, i, j):
        if 0 <= i < self.m and 0 <= j < self.n and self.grid[i][j] == '1':
            self.grid[i][j] = '0'
            for a, b in (i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1):
                self.findland(a, b)