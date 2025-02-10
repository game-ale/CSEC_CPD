
import math
W,Y = map(int,input().split())
dot = 6-max(W,Y)+1
gcdf = math.gcd(6,dot)
tot = 6//gcdf
dot = dot//gcdf
print(f"{dot}/{tot}")
