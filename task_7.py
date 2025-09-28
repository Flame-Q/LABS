s = input()

res = ""
symb = s[0]
count = 1
    
for i in range(1, len(s)):
    if s[i] == symb:
        count += 1
    else:
        result += symb + str(count)
        symb = s[i]
        count = 1
    
result += symb + str(count)
    
print(result)