t = input()
s = input()
i , j = 0,0
while i<len(t)and j<len(s):
    if t[i]==s[j]:
        i+=1
        j+=1
    else:
        j+=1
print(i+1)