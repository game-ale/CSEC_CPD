n, k = map(int, input().split())
a = list(map(int, input().split()))

total = sum(a)
if total % k != 0:
    print("No")
else:
    target = total // k
    result = []
    cur_sum = 0
    count = 0
    
    for num in a:
        cur_sum += num
        count += 1
        if cur_sum == target:
            result.append(count)
            cur_sum = 0
            count = 0
        elif cur_sum > target:
            print("No")
            break
    else:
        if len(result) == k:
            print("Yes")
            print(' '.join(map(str, result)))
        else:
            print("No")