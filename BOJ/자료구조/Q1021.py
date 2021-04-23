import sys
from collections import deque


# 1021번 문제. 회전하는 큐
'''
INPUT
10 3
1 2 3
=> 0
============
10 3
2 9 5
=> 8
============
32 6
27 16 30 11 6 23
=> 59
============
10 10
1 6 3 2 7 9 8 4 10 5
=> 14

'''


n, m = map(int, input().split())
a = deque(map(int, input().split()))

d = deque(range(1, n+1))
cnt = 0

while a:
    if d[0] == a[0]:
        d.popleft()
        a.popleft()
    elif d.index(a[0]) > len(d) // 2:
        while d[0] != a[0]:
            d.appendleft(d.pop())
            cnt += 1
        if d[0] == a[0]:
            continue
    else:
        while d[0] != a[0]:
            d.append(d.popleft())
            cnt += 1
        if d[0] == a[0]:
            continue

print(cnt)

