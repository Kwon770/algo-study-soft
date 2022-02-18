inf = int(1e9)

n, m = map(int, input().split())
graph = [[inf]*(n+1) for _ in range(n+1)]

for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 0

# 각 간선에 대해 value를 1로 초기화
for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1

for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
                graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])
cnt = 0 # 학생 수 를 세는 변수
for a in range(1, n+1):
    count = 0
    for b in range(1,n+1):
        if graph[a][b] != inf or graph[a][b] != inf:
            count += 1
    if count == n:
        cnt += 1
print(cnt)