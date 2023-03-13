
from collections import deque

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
child = [0, 0]
level = 2
time = 0
exp = 0

# 상, 좌, 우, 하
dx = [0, -1, 1, 0]
dy = [-1, 0, 0, 1]

for r in range(N):
    for c in range(N):
        if board[r][c] == 9:
            child = [r, c]
            board[r][c] = 0

while True:
    dist = []
    visit = [[False] * N for _ in range(N)]
    visit[child[0]][child[1]] = True
    queue = deque([[0, child]])
    if all(x == 0 or x >= level for i in range(N) for x in board[i]):
        break

    while queue:
        t, p = queue.popleft()
        for d in range(4):
            nx = p[1] + dx[d]
            ny = p[0] + dy[d]
            if not(0 <= ny < N and 0 <= nx < N) or visit[ny][nx] or board[ny][nx] > level:
                continue
            if board[ny][nx] == level or board[ny][nx] == 0:
                if visit[ny][nx]:
                    continue
                queue.append([t + 1, [ny, nx]])
                visit[ny][nx] = True
            elif board[ny][nx] < level:
                dist.append([ny, nx, t + 1])
    if len(dist) == 0:
        break
    dist.sort(key=lambda x: [x[2], x[0], x[1]])
    exp += 1
    child = [dist[0][0], dist[0][1]]
    time += dist[0][2]
    board[dist[0][0]][dist[0][1]] = 0
    if exp == level:
        exp = 0
        level += 1

print(time)


