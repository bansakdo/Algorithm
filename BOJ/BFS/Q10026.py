from collections import deque

N = int(input())
poster = [list(input()) for _ in range(N)]
answer = [0, 0]

dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]


def bfs(y, x):
    color = poster[r][c]
    queue = deque([[r, c]])
    while queue:
        y, x = queue.popleft()
        if visited[y][x] == 0:
            visited[y][x] = 1
            for d in range(4):
                nx = x + dx[d]
                ny = y + dy[d]
                if 0 <= nx < N and 0 <= ny < N and visited[ny][nx] == 0 and poster[ny][nx] == color:
                    queue.append([ny, nx])


visited = [[0] * N for _ in range(N)]
for r in range(N):
    for c in range(N):
        if visited[r][c] == 0:
            answer[0] += 1
            bfs(r, c)

for r in range(N):
    for c in range(N):
        if poster[r][c] == 'G':
            poster[r][c] = 'R'

visited = [[0] * N for _ in range(N)]
for r in range(N):
    for c in range(N):
        if visited[r][c] == 0:
            answer[1] += 1
            bfs(r, c)

print(*answer)
'''
N = list(map(int, list(str(input()).zfill(6))))
M = int(input())
now = 100
defect = list(map(int, input().split()))
avail = [n for n in range(10) if n not in defect]
lowest = min(avail)
highest = max(avail)
size = len(N)

for i in range(size):
    if N[:i + 1] == [0] * i:
        continue
    if int(N[i]) in defect:
        c_up = N.copy()
        c_down = N.copy()
        while c_up[i] not in avail:
            c_up[i] += 1
            if c_up[i] >= 10:
                if i != 0:
                    c_up[i - 1] += 1
                    c_up[i] -= 10
        for j in range(i + 1, size):
            c_up[j] = lowest

        while c_down[i] not in avail:
            c_down[i] -= 1
        for j in range(i + i, size):
            c_down[j] = highest
'''
'''
5657
3
6 7 8

'''
