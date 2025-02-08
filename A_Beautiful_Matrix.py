s = [[int(n) for n in input().split()]for i in range(5)]
ans = 0
for i in range(5):
    for j  in  range(5):
        if s[i][j]==1:
            ans = abs(2-i) + abs(2-j)
            break
print(ans)