'''
The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,
F(0) = 0,   F(1) = 1
F(N) = F(N - 1) + F(N - 2), for N > 1.
Given N, calculate F(N).

Example 1:

Input: 2
Output: 1
Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.
Example 2:

Input: 3
Output: 2
Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2.
Example 3:

Input: 4
Output: 3
Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3.

Note:
0 ≤ N ≤ 30.
'''
from typing import *
from collections import defaultdict
class Solution:
    # 내 답안 - 32ms (66%)
    fib_dic = defaultdict(int)
    fib_dic[0] = 0
    fib_dic[1] = 1

    def fib(self, N: int) -> int:
        if N in self.fib_dic.keys():
            return self.fib_dic[N]

        else:
            self.fib_dic[N] = self.fib(N - 1) + self.fib(N - 2)

        return self.fib_dic[N]
