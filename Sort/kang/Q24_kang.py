#!/usr/bin/env python
# coding: utf-8

# In[2]:


num = int(input())
data = list(map(int, input().split()))
data.sort()

print(data[(num-1)//2])


# In[ ]:




