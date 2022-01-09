def solution(food_times, k):
    i = 0
    while sum(food_times) != 0:
        if food_times[i] != 0:
            food_times[i] -= 1
            k -= 1

            if k == -1:
                
                return i+1
        
        i += 1
        if i == len(food_times):
            i = 0
        
    return -1


print(solution([3,1,2], 5))

