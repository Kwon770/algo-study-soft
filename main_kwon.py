# https://www.acmicpc.net/problem/18310
# 18310, 안테나
# Memory : 53508 KB, Time : 156 ms

# 가장 중간에 있는 집에 안테나를 설치하는 것이 늘 최선이므로, 가장 중간에 있는 집을 찾으면 끝이다
# 가장 중간 외에 반례가 있을 것 같은 느낌이 들지만, 반례는 없는 것이 힘든 점이다.

import sys
input=sys.stdin.readline

def solution(N, stages):
    answer = []
    fails = [0 for _ in range(N+2)]
    challenges = [0 for _ in range(N+2)]

    for stage in stages:
        fails[stage] += 1
        for i in range(1, stage+1):
            challenges[i] += 1

    failRate = []
    for idx, (fail, challenge) in enumerate(zip(fails, challenges)):
        if idx == 0 or idx == N+1:
            continue

        if challenge == 0:
            failRate.append((0, idx))
            continue

        failRate.append((-(fail / challenge), idx))
    failRate.sort()

    for f in failRate:
        answer.append(f[1])
    return answer


print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
print(solution(4, [4,4,4,4,4]))

# def solution(N, stages):
#     answer = []
#     fails = [0 for _ in range(N+1)]
#     challenges = [0 for _ in range(N+1)]
#
#     stages.sort()
#     prevStage = stages[0]
#     prevIdx = 0
#     for idx, stage in enumerate(stages):
#         if prevStage == stage:
#             continue
#
#         fails[prevStage] = idx - prevIdx
#         challenges[prevStage] = len(stages) - prevStage
#         prevStage = stage
#         prevIdx = idx
#
#     for i in range(fails):
#         fails[i] = (-(fails[i][0] / challenges[i][0]), challenges[i][1])
#     fails.sort()
#
#     for f in fails:
#         answer.append(f[0])
#     return answer