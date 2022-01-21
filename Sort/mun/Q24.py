## 53508KB	168MS

num = int(input()) ##집의 수


house = list(map(int, input().split()))
house.sort()

##house 리스트의 중간값 출력
print(house[(num-1)//2])