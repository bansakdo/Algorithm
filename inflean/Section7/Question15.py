import sys
import copy
from collections import deque

sys.stdin = open("input.txt", "rt")

# 15번 문제. 토마토 보

# 내 풀이
'''
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

m, n = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(n)]
ch = [[0] * m for _ in range(n)]
# print(box)
# print(ch)

def DFS(x, y):
    rst = False
    ch[x][y] = 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if box[nx][ny] == 0 and ch[nx][ny] == 0:
                rst = DFS(nx, ny)
            elif box[nx][ny] == -1:
                continue
            elif box[nx][ny] == 1 or ch[nx][ny] == 1:
                return True
        if rst:
            return rst
    return rst


cnt = 0
isChecked = False



while True:
    tbox = copy.deepcopy(box)
    isDone = True
    # print()
    # for i in range(n):
    #     print(box[i])

    for i in range(n):
        for j in range(m):
            if box[i][j] == 1:
                for k in range(4):
                    x = i + dx[k]
                    y = j + dy[k]
                    if 0 <= x < n and 0 <= y < m and box[x][y] == 0:
                        isDone = False
                        tbox[x][y] = 1
            if not isChecked and box[i][j] == 0 and ch[i][j] == 0:
                # print("=====")
                # print(i, j)
                # for z in range(n):
                #     print(ch[z])
                # ch = [[0] * m for _ in range(n)]
                rst = DFS(i, j)
                if not rst:
                    print(-1)
                    sys.exit(1)

    if isDone:
        break
    cnt += 1
    isChecked = True
    box = copy.deepcopy(tbox)

print(cnt)
'''


# 해설
'''
queue를 사용하여 bfs 사용
'''
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(m)]
Q = deque()
dis = [[0] * n for _ in range(m)]

for i in range(m):
    for j in range(n):
        if board[i][j] == 1:
            Q.append((i, j))
while Q:
    tmp = Q.popleft()
    for i in range(4):
        xx = tmp[0] + dx[i]
        yy = tmp[1] + dy[i]

        if 0 <= xx < m and 0 <= yy < n and board[xx][yy] == 0:
            board[xx][yy] = 1
            dis[xx][yy] = dis[tmp[0]][tmp[1]] + 1
            Q.append((xx, yy))
flag = 1

for i in range(m):
    for j in range(n):
        if board[i][j] == 0:
            flag = 0
result = 0
if flag == 1:
    for i in range(m):
        for j in range(n):
            if dis[i][j] > result:
                result = dis[i][j]
    print(result)
else:
    print(-1)
