# 내장 이진 탐색 함수를 응용하는 문제

import bisect
import sys
input=sys.stdin.readline

n, x = map(int, input().split())
arr = list(map(int, input().split()))

left = bisect.bisect_left(arr, x)
right = bisect.bisect_right(arr, x)

if left == right:
    print(-1)
else:
    print(right - left)