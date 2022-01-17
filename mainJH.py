food_times = list(map(int, input()))
print(food_times)
k = int(input())## 남은 시간
sum = sum(food_times) ## 남은 음식의 양
food_num = len(food_times) ##남은 음식 종류의 수

def solution(food_times, sum, k):
    if sum < k:
        return -1

    for i in food_times:
        i = i-1
        k -=1
        if sum ==0 :
            return -1
        if k ==0:
            return i

solution(food_times, sum, k)