#!/usr/bin/env python
# coding: utf-8

# In[55]:


str = input()
cnt1 =0
cnt0 = 0
if str[0] == '0':
    cnt1 += 1
else:
    cnt0 += 1
for i in range(len(str)-1):
    if str[i] != str[i+1] and str[i+1] == '1' :
        cnt0 += 1
    elif str[i] != str[i+1] and str[i+1] == '0':
        cnt1 += 1

print(min(cnt1, cnt0))

