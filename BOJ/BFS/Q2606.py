
from collections import deque

N = int(input())
M = int(input())
network = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    network[a-1].append(b-1)
    network[b-1].append(a-1)

rst = [0]
queue = deque([0])

while queue:
    now = queue.popleft()
    for x in network[now]:
        if x in rst:
            continue
        rst.append(x)
        queue.append(x)

print(len(rst) - 1)




