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
    n = I()
    nums = LI()
    x = abs(nums[0]-nums[1])
    if n==2:
        return x
    y = min ( x + abs(nums[1]-nums[2]), abs(nums[0]-nums[2]))
    for i in range(3,n):
        z = min(x+abs(nums[i]-nums[i-2]), y + abs(nums[i-1]- nums[i]))
        x = y
        y = z
    return y
        

def main():
    t = 1
    # t = I()
    for _ in range(t):
        print(solve())

if __name__ == "__main__":
    main()