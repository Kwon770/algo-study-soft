#!/usr/bin/env python
# coding: utf-8

# In[4]:


##이진 탐색으로 mid의 값과 입력된 배열 arr[mid]의 값이 같으면 mid값을 return
##고정점이 단 하나만 존재하기 때문에 가능

n = int(input())
arr = list(map(int, input().split()))

def solution(array,start,end):
    if start > end:
        return -1
    mid = (start + end)//2
    
    if array[mid] == mid:
        return mid
    elif array[mid] > mid:
        return solution(array,start,mid-1)
    else:
        return solution(array, mid+1,end)
    
print(solution(arr,0,n-1))

