# Memory : 30846 KB Time : 68 ms

inp = input()
left = 0
right = 0
for idx, num in enumerate(inp):
    if idx < len(inp)/2:
        left += int(num)
    else:
        right += int(num)
      
if left == right:
    
    print("LUCKY")
else:
    print("READY")
    
