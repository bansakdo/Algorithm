import sys

# 상 우 하 좌
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
N = int(input())
matrix = [list(input()) for _ in range(N)]
rst = 0

for x in range(N):
    for y in range(N):
        std = matrix[x][y]

        # 열 탐색
        cnt = 1
        lt, rt = y - 1, y + 1
        while lt >= 0 and matrix[x][lt] == std:
            cnt += 1
            lt -= 1
        while rt < N and matrix[x][rt] == std:
            cnt += 1
            rt += 1
        rst = max(rst, cnt)

        # 행 탐색
        cnt = 1
        lt, rt = x - 1, x + 1
        while lt >= 0 and matrix[lt][y] == std:
            cnt += 1
            lt -= 1
        while rt < N and matrix[rt][y] == std:
            cnt += 1
            rt += 1
        rst = max(rst, cnt)

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and matrix[x][y] != matrix[nx][ny]:
                matrix[x][y], matrix[nx][ny] = matrix[nx][ny], matrix[x][y]
                std = matrix[x][y]
                cnt = 1
                lt, rt = y - 1, y + 1
                while lt >= 0 and matrix[x][lt] == std:
                    cnt += 1
                    lt -= 1
                while rt < N and matrix[x][rt] == std:
                    cnt += 1
                    rt += 1
                rst = max(rst, cnt)
                cnt = 1
                lt, rt = x - 1, x + 1
                while lt >= 0 and matrix[lt][y] == std:
                    cnt += 1
                    lt -= 1
                while rt < N and matrix[rt][y] == std:
                    cnt += 1
                    rt += 1
                rst = max(rst, cnt)
                matrix[x][y], matrix[nx][ny] = matrix[nx][ny], matrix[x][y]

                if rst == N:
                    print(rst)
                    sys.exit()

print(rst)
