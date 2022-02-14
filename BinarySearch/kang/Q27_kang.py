#!/usr/bin/env python
# coding: utf-8

# In[3]:


from bisect import bisect_left, bisect_right

n, x = map(int, input().split())
arr = list(map(int, input().split()))

first_index = bisect_left(arr,x)
last_index = bisect_right(arr,x)

result = last_index-first_index
if result == 0:
    print(-1)
else:
    print(result)

