string = input()

zero_part = 0
one_part = 0
prev_part = -1
    

for char in string:
    if prev_part != char:    
        if char == "0":
            zero_part += 1
        else:
            one_part += 1
            
            
    prev_part = char
    
            
print(min(zero_part, one_part))
