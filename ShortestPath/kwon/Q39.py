# ShortestPath - Q39 화성탐사 (P388)

import sys; input = sys.stdin.readline
import heapq

INF = int(1e9)

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

def dijkstra():
    q = []
    heapq.heappush(q, (0, mars[0][0]))
    distance = [INF] * (N*N)
    distance[0] = mars[0][0]
    while q:
        now, dist = heapq.heappop(q)
        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (i[0], cost))

    return distance[N*N-1]

def solution():
    global N, mars, graph

    for T in range(int(input())):
        N = int(input())
        mars = []
        for r in range(N):
            arr = list(map(int, input().split()))
            mars.append(arr)

        graph = [[] for _ in range(N*N)]
        for r in range(N):
            for c in range(N):
                for i in range(4):
                    nr = r + dr[i]
                    nc = c + dc[i]
                    if nr < 0 or nc < 0 or nr >= N or nc >= N:
                        continue

                    fromIdx = N*r + c
                    toIdx = N*nr + nc
                    graph[fromIdx].append((toIdx, mars[nr][nc]))

        print(dijkstra())

solution()
