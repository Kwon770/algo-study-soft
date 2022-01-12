inp = input()

alphabets = [0 for _ in range(91)]
nums = 0

for char in inp:
    if ord(char) < 65:
        nums += int(char)
    else:
        
        alphabets[ord(char)] += 1

for i in range(1, 91):
    for j in range(alphabets[i]):
        print(chr(i), end="")
print(nums)
