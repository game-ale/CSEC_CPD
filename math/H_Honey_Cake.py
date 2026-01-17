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
def honey_cake(w, h, d, n):
    wc, hc, dc = 1, 1, 1
    pieces = 1
    
    while pieces < n:
        if wc * 2 <= w and pieces * 2 <= n:
            wc *= 2
            pieces *= 2
        elif hc * 2 <= h and pieces * 2 <= n:
            hc *= 2
            pieces *= 2
        elif dc * 2 <= d and pieces * 2 <= n:
            dc *= 2
            pieces *= 2
        else:
            break
    
    if pieces == n:
        print(wc, hc, dc)
    else:
        print(-1)
def solve():
    w,h,d = II()
    n = I()
    honey_cake(w, h, d, n)
    
    

def main():
    t = 1
    # t = I()
    for _ in range(t):
        solve()

if __name__ == "__main__":
    main()

