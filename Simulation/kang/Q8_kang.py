#!/usr/bin/env python
# coding: utf-8

# In[30]:


strinput = input()

list_alpha = []
list_num=[]
sum = 0
for i in range(len(strinput)):
    if ord(strinput[i]) >= 65:
        list_alpha.append(strinput[i])
    else:
        list_num.append(int(strinput[i]))
for i in range(len(list_num)):
    sum += list_num[i]

result = "".join(sorted(list_alpha)) + "{}".format(sum)
print(result)

