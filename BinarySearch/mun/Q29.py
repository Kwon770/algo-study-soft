##왜 답이 안나오는지 모르겠습니다..

import sys

n, c = map(int, sys.stdin.readline().split())
house=[int(sys.stdin.readline()) for _ in range(n)]

house.sort()

#공유기 사이 거리 최솟값
start = 1
#공유기 사이 거리 최댓값
end = house[n-1]-house[0]
answer =0

def binary_serch(house, start, end):
    while start<=end :
        count = 1
        mid = (start+end)//2
        current = house[0] #공유기가 설치된 집의 위치
        for x in house:
            if current + mid <=x: # 공유기 설치
                count +=1
                current = x
            if count>=c : # mid값에 따라 설치된 공유기의 개수가 c보다 많거나 같으면
                start = mid+1 #거리를 늘린다.
                global answer
                answer = mid
            else:
                end = mid -1 #c보다 작으면 거리를 줄인다.

binary_serch(house, start, end)
print(answer)