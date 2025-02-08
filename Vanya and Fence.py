ans = 0
n,h  = map(int,input().split())
element = list(map(int,input().split()))
for  ele in element:
    if ele>h:
        ans+=2
    else:
        ans+=1
print(ans)
