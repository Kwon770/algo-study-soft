## 시간초과,,,,,?

num = int(input())  ##묶음의 수

## 묶음 추가
arr = []
for i in range(num):
    arr.append(int(input()))

## 묶음의 수가 1개일 경우 비교하지 않아도 된다.
sum = 0
while len(arr)>1:

    arr.sort()
    a = arr[0]
    del arr[0]
    b = arr[0]
    del arr[0]
    arr.append(a+b)
    sum +=(a+b)

print(sum)
