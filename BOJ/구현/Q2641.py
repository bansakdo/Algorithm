
from collections import deque

n = int(input())
std_arr = deque(map(int, input().split()))
m = int(input())
arrs = list(deque(map(int, input().split())) for _ in range(m))
rst = []
for i in range(m):
    c_arr = arrs[i].copy()
    for j in range(n):
        if c_arr == std_arr:
            rst.append(list(arrs[i]))
            break
        c_arr.append(c_arr.popleft())
    else:
        c_arr = deque([(x + 1) % 4 + 1 for x in arrs[i]])
        c_arr.reverse()
        for j in range(n):
            if c_arr == std_arr:
                rst.append(list(arrs[i]))
            c_arr.append(c_arr.popleft())

print(len(rst))
for arr in rst:
    print(*arr)