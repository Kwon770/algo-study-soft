num = int(input()) ## 입력받을 데이터의 수

arr = []
for _ in range(num):
    arr.append(int(input())) ## num의 수만큼 데이터 입력 받기

arr.sort(reverse=True)

for i in arr:
    print(i, end = " ")