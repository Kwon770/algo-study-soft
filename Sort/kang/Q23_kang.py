#!/usr/bin/env python
# coding: utf-8

# In[20]:


num = int(input())
list1 = []
for i in range(num):
    name, a, b, c =input().split()
    list1.append([name,int(a),int(b),int(c)])
    

list1.sort(key = lambda x : (-x[1], x[2], -x[3], x[0]))

for i in list1:
    print(i[0])


# In[ ]:




