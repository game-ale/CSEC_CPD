n = input()
cnt_capital = 0
cnt_lower = 0
for i in range(len(n)):
    if n[i].isupper():
        cnt_capital+=1
    else:
        cnt_lower+=1
if cnt_capital>cnt_lower:
    print(n.upper())
else:
    print(n.lower())