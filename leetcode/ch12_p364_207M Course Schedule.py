'''
There are a total of numCourses courses you have to take, labeled from 0 to numCourses-1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?



Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take.
             To take course 1 you should have finished course 0. So it is possible.
Example 2:

Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take.
             To take course 1 you should have finished course 0, and to take course 0 you should
             also have finished course 1. So it is impossible.


Constraints:

The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented.
You may assume that there are no duplicate edges in the input prerequisites.
1 <= numCourses <= 10^5
'''
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # 내 풀이 - 1260ms (5%)
        self.len_mydict = -1
        self.mydict = {}

        for course in range(numCourses):
            self.mydict[course] = []
        for course, pre in prerequisites:
            self.mydict[course].append(pre)

        while self.mydict:
            self.endnode = []
            for i in self.mydict:
                if self.mydict[i] == []:
                    self.endnode.append(i)

            for i in self.endnode:
                del self.mydict[i]

            for i in self.mydict:
                self.mydict[i] = list(set(self.mydict[i]) - set(self.endnode))

            if len(self.mydict) == self.len_mydict:
                print(self.mydict)
                return False

            self.len_mydict = len(self.mydict)

        return True