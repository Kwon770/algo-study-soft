# https://programmers.co.kr/learn/courses/30/lessons/60060
# 2020 KAKAO BLUND RECRUITMENT, 가사 검색

import sys
input = sys.stdin.readline
import heapq

INF = int(1e9)

def getDistanceByDijkstra(start, end):
    distance = [INF] * (n + 1)
    visited = [False] * (n + 1)
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue

        for node in graph[now]:
            cost = dist + node[0]
            if cost < distance[node[1]]:
                distance[node[1]] = cost
                heapq.heappush(q, (cost, node[1]))

    return distance[end]

def solution():
    global n, m, graph
    n, m = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append((1, b))
        graph[b].append((1, a))
    x, k = map(int, input().split())

    toK = getDistanceByDijkstra(1, k)
    toX = getDistanceByDijkstra(k, x)
    if toK >= INF or toX >= INF:
        print(-1)
    else:
        print(toK + toX)


print(solution())