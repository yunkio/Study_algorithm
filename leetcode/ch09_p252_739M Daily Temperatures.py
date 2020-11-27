'''
Given a list of daily temperatures T, return a list such that, for each day in the input, tells you how many days you would have to wait until a warmer temperature. If there is no future day for which this is possible, put 0 instead.

For example, given the list of temperatures T = [73, 74, 75, 71, 69, 72, 76, 73], your output should be [1, 1, 4, 2, 1, 1, 0, 0].

Note: The length of temperatures will be in the range [1, 30000]. Each temperature will be an integer in the range [30, 100].
'''

from typing import *
class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        # 내 풀이 - 520ms, 35%
        n = len(T)
        wait = [0] * n
        closest = [n-1]
        for i in range(n-2, -1, -1):
            if T[i+1] > T[i]:
                wait[i] = 1
            else:
                while closest:
                    j = closest[-1]
                    if T[j] > T[i]:
                        wait[i] = j - i
                        break
                    else:
                        closest.pop()
            closest.append(i)
        return wait
