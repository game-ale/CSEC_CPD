n = int(input().strip())
birds = list(map(int, input().strip().split()))
m = int(input().strip())
for _ in range(m):
    xi, yi = map(int, input().strip().split())
    index = xi - 1
    bird_pos = yi - 1
    if index > 0:
        birds[index - 1] += bird_pos
    if index < n - 1:
        birds[index + 1] += (birds[index] - bird_pos - 1)
    birds[index] = 0
for count in birds:
    print(count)
