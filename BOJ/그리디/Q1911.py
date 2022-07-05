import sys
import math

N, L = map(int, sys.stdin.readline().split())
water = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
water.sort()
ready = [water[0]]
for i in range(1, N):
    if water[i][0] <= ready[-1][1] or ((ready[-1][1] - ready[-1][0]) % L != 0 and water[i][0] - ready[-1][1] <= L - ((ready[-1][1] - ready[-1][0]) % L)):
        ready[-1][1] = max(ready[-1][1], water[i][1])
    else:
        ready.append(water[i])
rst = 0
for a, b in ready:
    rst += math.ceil((b - a) / float(L))
print(rst)


'''
3 3
1 6
14 16
8 14
9 15


'''
