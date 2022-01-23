#!/usr/bin/env python
# coding: utf-8

# In[5]:


def solution(N, stages):
    answer = []
    cnt = 0
    player = len(stages)
    
    for i in range(1,N+1):
        cnt = stages.count(i)
        if cnt == 0 :
            answer.append((i,0))
        else:
            answer.append((i,cnt/player))
        player = player-cnt
        
    answer.sort(key=lambda x : x[1], reverse = True)
    answer = [i[0] for i in answer]
    return answer

print(solution(5,[2, 1, 2, 6, 2, 4, 3, 3]))
print(solution(4,[4,4,4,4,4]))

