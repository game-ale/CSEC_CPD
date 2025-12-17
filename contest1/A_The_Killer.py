a, b , c = map(int , input().split())
ans = 0
for i in range (1,c+1):
    if i%a==0 and i%b==0:
        ans+=1
print(ans)
    
    