'''
You are given an array of people, people, which are the attributes of some people in a queue (not necessarily in order). Each people[i] = [hi, ki] represents the ith person of height hi with exactly ki other people in front who have a height greater than or equal to hi.

Reconstruct and return the queue that is represented by the input array people. The returned queue should be formatted as an array queue, where queue[j] = [hj, kj] is the attributes of the jth person in the queue (queue[0] is the person at the front of the queue).



Example 1:

Input: people = [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]
Output: [[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]]
Explanation:
Person 0 has height 5 with no other people taller or the same height in front.
Person 1 has height 7 with no other people taller or the same height in front.
Person 2 has height 5 with two persons taller or the same height in front, which is person 0 and 1.
Person 3 has height 6 with one person taller or the same height in front, which is person 1.
Person 4 has height 4 with four people taller or the same height in front, which are people 0, 1, 2, and 3.
Person 5 has height 7 with one person taller or the same height in front, which is person 1.
Hence [[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]] is the reconstructed queue.
Example 2:

Input: people = [[6,0],[5,0],[4,0],[3,2],[2,2],[1,4]]
Output: [[4,0],[5,0],[2,2],[3,2],[1,4],[6,0]]


Constraints:

1 <= people.length <= 2000
0 <= hi <= 106
0 <= ki < people.length
It is guaranteed that the queue can be reconstructed.
'''
from typing import *
from collections import Counter
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # 내 풀이 - Time Limit Exceeded
        task_set = set(tasks)
        task_delay = dict(zip(task_set, [0] * len(task_set)))
        task_num = Counter(tasks)
        task_num['idle'] = 0
        res = len(tasks)
        while list(task_num.values())[0] > 0:
            task_num = dict(sorted(task_num.items(), key=lambda x: -x[1]))
            for task in task_num:
                if task_num[task] <= 0:
                    print('idle')
                    res += 1
                    break
                elif task_delay[task] <= 0:
                    print('task in : ' + task)
                    task_num[task] -= 1
                    task_delay[task] = n + 1
                    break

            for task in task_delay:
                task_delay[task] -= 1
        return res

    def leastInterval(self, tasks: List[str], n: int) -> int:
        # 다시 풀이 - 384ms (86%)
        count_list = list(Counter(tasks).values())
        max_count = max(count_list)
        max_count_num = count_list.count(max_count)

        return max((n+1) * (max_count-1) + max_count_num, len(tasks))