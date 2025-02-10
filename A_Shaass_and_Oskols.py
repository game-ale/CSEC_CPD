# n = int(input())
# arr = list(map(int,input().split()))
# m = int(input())
# arr2 = [[int (n) for n in input().split()] for i in range (m)]
# for num in arr2:
#     if num[0]-1>=0 and num[0]+1<m:
#         arr[num[0]-1]+=num[1]-1
#         arr[num[0]+1]+=arr[num[0]]-num[1]
#         arr[num[0]]=0
#     elif num[0]-1>=0:
#         arr[num[0]-1]+=num[1]-1
#         arr[num[0]]=0
#     elif num[0]+1<m:
#         arr[num[0]+1]+=arr[num[0]]-num[1]
#         arr[num[0]]=0
#     else:
#         arr[num[0]]=0
# for num in arr:
#     print(num)

        

n = int(input().strip())
birds = list(map(int, input().strip().split()))
m = int(input().strip())

for _ in range(m):
    xi, yi = map(int, input().strip().split())
    wire_index = xi - 1
    bird_position = yi - 1

    if wire_index > 0:
        birds[wire_index - 1] += bird_position

    if wire_index < n - 1:
        birds[wire_index + 1] += (birds[wire_index] - bird_position - 1)

    birds[wire_index] = 0

for count in birds:
    print(count)
