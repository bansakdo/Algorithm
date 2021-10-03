from collections import deque


N, M = map(int, input().split())
arr = list(map(int, input().split()))

queue = deque([])
tot = 0
cnt = 0

for idx in range(N):
    queue.append(arr[idx])
    tot += queue[-1]

    while tot >= M or idx == N - 1:
        if tot == M:
            cnt += 1
        if not queue:
            break
        tot -= queue.popleft()

print(cnt)






