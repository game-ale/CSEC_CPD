

s = input()
ans = 0
cur_pos = ord('a')
for i in range(len(s)):

    destination= ord(s[i])
    clock = abs(destination-cur_pos)
    count_clock = 26 - clock
    ans+=min(clock,count_clock)
    cur_pos = destination
print(ans)
