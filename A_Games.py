
n = int(input())
res = [[int(t) for t in input().split()]for i in range(n)]
ans = 0
for i in range(len(res)):
    for j  in range(len(res)):
        if res[i][1]==res[j][0]:
            ans+=1
print(ans)