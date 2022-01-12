##30864KB   68MS

score = list(map(int, input()))
score_len = len(score)
sum1 = 0
sum2 =0
for i in range(int(score_len/2)):
    sum1 += score[i]

for i in range(int(score_len/2)):
    sum2 += score[i+int(score_len/2)]

if (sum1 == sum2):
    print("LUCKY")
else:
    print("READY")