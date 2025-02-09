n = int(input())
l = list(map(int,input().split()))
pos,neg,ans = 0,0,0
for i in range(len(l)):
    if l[i]< 0 and pos + l[i]<0:
        ans+=abs(pos + l[i])
    elif l[i]>0:
        pos+=l[i]
    elif l[i]<0:
        pos+=l[i]
print(ans)


