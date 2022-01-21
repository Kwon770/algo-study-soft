## 62904KB	4764ms


num = int(input())  ##n명의 학생 수
arr = []
## n명의 학생의 데이터 입력받기
for i in range(num):
    name, korea, english, math = list(map(str, input().split()))
    arr.append([name, int(korea), int(english),int(math)])

arr.sort(key = lambda x : (-x[1], x[2], -x[3], x[0]))

for i in arr:
    print (i[0])