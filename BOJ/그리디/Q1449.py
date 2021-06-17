import sys
from collections import deque

n, l = map(int, sys.stdin.readline().split())
leak = list(map(int, sys.stdin.readline().split()))

leak = deque(sorted(leak))

num = 0

while leak:
    start = leak.popleft()
    num += 1

    while leak and leak[0] - start <= l - 1:
        leak.popleft()

print(num)









