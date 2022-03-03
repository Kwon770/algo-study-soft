#!/usr/bin/env python
# coding: utf-8

# In[ ]:


##무한을 의미하는 값
INF = int(1e9) 

##노드의 개수 및 간선의 개수 입력 받기
n = int(input()) 
m = int(input()) 

##2차원 리스트를 만들고, 모든 값을 무한으로 초기화
graph = [[INF]*(n+1) for _ in range(n+1)]


##자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화

for a in range(1, n+1):
    for b in range(1,n+1):
        if a == b:
            graph[a][b]=0

#각 간선에 대한 정보를 입력받아, 그 값으로 초기화             
for _ in range(m):
    a, b, c = map(int,input().split())
    if graph[a][b] == INF: ##이때 초기화하는 값이 INF이면 
        graph[a][b] = c ##그대로 c값으로 초기화하고 
        
    else: ##값이 INF가 아니라면 
        graph[a][b] = min(c, graph[a][b]) ##이전에 저장한 값과 현재 입력받는 값 중에서 더 작은 값으로 초기화한다.
                                          ##이 문장은 문제에서 '시작도기와 도착 도시를 연결하는 노선은 하나가 아닐 수 있습니다' 
                                          ##라는 입력 조건이 있기 때문에 필요한 코드이다.
                                          ##만약 이 비교하는 코드가 없다면 이전에 입력된 비용값이 더 작아도 나중에 입력한 값으로
                                          ##무조건 비용이 초기화되어 구하려는 최소 비용을 구하지 못하게 될 수 있다.
    
##플로이드 워셜 알고리즘 수행   
for k in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            graph[a][b] = min(graph[a][b],graph[a][k]+graph[k][b])

##수행된 결과를 출력             
for a in range(1, n+1):
    for b in range(1, n+1):
        if graph[a][b] >= INF:
            print("0", end=" ")
        else:
            print(graph[a][b], end = " ")
    print()
                

