'''
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.


Constraints:

1 <= intervals.length <= 104
intervals[i].length == 2
0 <= starti <= endi <= 104
'''
class Solution:
    # 내 풀이 - 84ms (75%)
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return
        intervals.sort()
        result = [intervals[0]]
        for i in range(1, len(intervals)):
            if result[-1][1] < intervals[i][0]:
                result.append(intervals[i])
            elif result[-1][1] < intervals[i][1]:
                result[-1][1] = intervals[i][1]
        return result