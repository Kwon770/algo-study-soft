alpha = list()
data = list(input())
sum = 0

for i in range(len(data)):
    if ord(data[i])>=48 and ord(data[i])<=57 : ##숫자일 경우
        sum += int(data[i])
    else:
        alpha.append(data[i])

print("".join(sorted(alpha, reverse=False))+str(sum))
