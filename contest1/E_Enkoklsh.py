import sys, math, bisect, heapq, itertools
from collections import defaultdict, deque, Counter

# --- INPUT HELPERS ---
def I(): return int(sys.stdin.readline())
def II(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def SI(): return sys.stdin.readline().strip()
def LSI(): return list(sys.stdin.readline().strip())
def INF(): return float('inf')

# --- MAIN LOGIC ---
def solve():
    k = int(input())
    a = list(map(int, input().split()))

    week_sum = sum(a)

    full_weeks = k // week_sum
    rem = k % week_sum

    a2 = a + a
    n = 7

    if rem == 0:
        need = week_sum
    else:
        need = rem

    left = 0
    cnt = 0
    best = 10**18

    for right in range(2 * n):
        cnt += a2[right]
        while cnt >= need:
            best = min(best, right - left + 1)
            cnt -= a2[left]
            left += 1
    if rem:
        print(full_weeks * 7 + best)
    else:
          print(full_weeks * 7 + best-7)
        
            
        
        
        
    

def main():
    t = 1
    t = I()
    for _ in range(t):
        solve()

if __name__ == "__main__":
    main()