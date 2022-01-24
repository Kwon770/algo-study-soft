num = int(input()) ## 입력받을 데이터 수

arr =[]
for _ in range(num):
    student = input().split()
    arr.append((student[0], int(student[1])))


result = sorted(arr, key= lambda arr :arr[1])

for i in result:
    print(i[0], end = " ")