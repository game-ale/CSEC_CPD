a1,a2,a3,a4 = map(int, input().split())
s = input()
ans = 0
for i in range(len(s)):
    if s[i]=='1':
        ans+=a1
    elif s[i]=='2':
        ans+=a2
    elif s[i]=='3':
        ans+=a3
    else:
        ans+=a4
print(ans)