
from collections import deque

M, N, K = map(int, input().split())
squares = [list(map(int, input().split())) for _ in range(K)]

board = [[0 for _ in range(N)] for _ in range(M)]
chk = [[0 for _ in range(N)] for _ in range(M)]
rst = []

for x1, y1, x2, y2 in squares:
    for y in range(y1, y2):
        for x in range(x1, x2):
            board[y][x] = 1

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

for i in range(M):
    for j in range(N):
        if board[i][j] == 0 and chk[i][j] == 0:
            queue = deque([[i, j]])
            cnt = 0
            while queue:
                y, x = queue.popleft()

                if board[y][x] == 0 and chk[y][x] == 0:
                    cnt += 1
                    chk[y][x] = 1

                    for d in range(4):
                        ny = y + dy[d]
                        nx = x + dx[d]

                        if 0 <= ny < M and 0 <= nx < N and board[ny][nx] == 0 and chk[ny][nx] == 0:
                            queue.append([ny, nx])

            rst.append(cnt)

rst.sort()
print(len(rst))
print(*rst)





