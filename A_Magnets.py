n = int(input())
ans = 0
temp = ""
for i in range(n):
    s = input()
    if not temp or temp[-1]==s[0]:
        ans+=1
        temp+=s
    else:
        temp+=s
print(ans)
    
