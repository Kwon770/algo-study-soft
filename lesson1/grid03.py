s= input()

count1 = 0
count0 = 0
for i in s.split("1"):
    if i != '':
        count1+=1

for i in s.split("0"):
    if i != '':
        count0 += 1
print(min(count0,count1))

