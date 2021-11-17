import sys
from collections import deque
sys.stdin = open("input.txt", "rt")

# 5번 문제. 공주 구하기 (큐 자료구조로 해결)

# 내 풀이
'''
n, k = map(int, input().split())

prince = [x for x in range(1, n + 1)]
idx = 0
for i in range(n - 1):
    idx += k-1
    idx %= len(prince)
    prince.pop(idx)

print(prince[0])
'''


# 해설
'''
# Queue : FIFO(First In First Out)
# deque가 queue 구조.
n, k = map(int, input().split())
dq = list(range(1, n+1))
dq = deque(dq)
while dq:
    for _ in range(k - 1):
        cur = dq.popleft()
        dq.append(cur)
    dq.popleft()
    if len(dq) == 1:
        print(dq[0])
        dq.popleft()
'''



