#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def solution(food_times, k):
    allfood = []
    
    for i in range(len(food_times)):
        allfood.append((food_times[i]),i+1)
        
    allfood.sort() ##여기까지,,,,
    
    answer = 0
    return answer

