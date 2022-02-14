# logN 알고리즘을 요구하며, 고정점이 단 하나라는 점이 이진 탐색의 단서이다.

import sys
input=sys.stdin.readline

def solve():
    global arr
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (high + low) // 2
        if mid == arr[mid]:
            print(mid)
            return

        if mid > arr[mid]:
            low = mid + 1
        else:
            high = mid - 1

    print(-1)


n = int(input())
arr = list(map(int, input().split()))
solve()
