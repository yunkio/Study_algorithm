'''

문제
N개의 수로 된 수열 A[1], A[2], …, A[N] 이 있다. 이 수열의 i번째 수부터 j번째 수까지의 합 A[i] + A[i+1] + … + A[j-1] + A[j]가 M이 되는 경우의 수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 N(1 ≤ N ≤ 10,000), M(1 ≤ M ≤ 300,000,000)이 주어진다. 다음 줄에는 A[1], A[2], …, A[N]이 공백으로 분리되어 주어진다. 각각의 A[x]는 30,000을 넘지 않는 자연수이다.

출력
첫째 줄에 경우의 수를 출력한다.

예제 입력 1
4 2
1 1 1 1
예제 출력 1
3
예제 입력 2
10 5
1 2 3 4 2 5 3 1 1 2
예제 출력 2
3
'''

# 내 풀이 - 836ms 느리다

N, M = map(int, input().split(' '))
nums = list(map(int, input().split(' ')))

answer = 0
for i in range(len(nums)):
    mynums = nums[i:]
    j = 0
    target = M
    if sum(mynums) >= M:
        for j in range(len(mynums)):
            target -= mynums[j]
            if target == 0:
                answer += 1
                break
            elif target < 0:
                break
print(answer)

### 모범 풀이 - 60ms

# n, m = map(int, input().split())
# a = list(map(int, input().split()))
# k, p, c = 0, 0, 0
#
# for i in a:
#     p += i
#     while p > m:
#         p -= a[k]
#         k += 1
#     c += (p == m)
#
# print(c)