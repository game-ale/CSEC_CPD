n = input()
m = input()
ans = 0
for i in range (len(n)):
    if n[i].lower()>m[i].lower():
        ans = 1
        break
    elif n[i].lower()<m[i].lower():
        ans = -1
        break
print(ans)
