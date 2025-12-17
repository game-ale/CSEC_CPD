from collections import defaultdict
jobs = defaultdict(list)
n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

for i in range(n):
    jobs[a[i]].append(b[i])

ans = []
for job in range(1, k + 1):
    if job in jobs:
        jobs[job].sort()
        ans.extend(jobs[job][:-1])

ans.sort()
result = sum(ans[:k - len(jobs)])
print(result)