#!/usr/bin/env python
# coding: utf-8

#메모리: 30864KB 시간: 72ms


# In[23]:


inputnum = input()

div_num = [inputnum[:len(inputnum)//2],inputnum[len(inputnum)//2:]]
a = []
sum_left =0
sum_right = 0

for i in range(2):
    line = []              
    for j in range(len(inputnum)//2):
        line.append(int(div_num[i][j]))     
    a.append(line)        

for i in range(len(inputnum)//2):
    sum_left += a[0][i]
for i in range(len(inputnum)//2):
    sum_right += a[1][i] 

if (sum_left == sum_right):
    print('LUCKY')
else:
    print('READY')

