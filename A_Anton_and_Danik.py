from collections import Counter
 
n = int(input())
s = input()
cnt = Counter(s)
if cnt['A']>cnt['D']:
    print("Anton")
elif cnt['D']>cnt["A"]:
    print("Danik")
else:
    print("Friendship")
    