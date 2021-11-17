import sys
from collections import deque

sys.stdin = open("input.txt", "rt")


# 13번 문제. 섬나라 아일랜드 (BFS 활용)

# 내 풀이
'''
dx = [-1, 0, 1, 0, -1, -1, 1, 1]
dy = [0, 1, 0, -1, -1, 1, -1, 1]

def DFS(n_x, n_y):
    island[n_x][n_y] = 0
    for i in range(8):
        xx = n_x + dx[i]
        yy = n_y + dy[i]

        if 0 <= xx < n and 0 <= yy < n and island[xx][yy] == 1:
            DFS(xx, yy)


n = int(input())
island = []
for _ in range(n):
    island.append(list(map(int, input().split())))

cnt = 0

for i in range(n):
    x = i
    for j in range(n):
        y = j
        if island[i][j] == 1:
            cnt += 1
            DFS(i, j)

print(cnt)
'''


# 해설
'''
BFS를 이용하여 풀이
BFS를 이용하기 때문에 deque 사용.
'''
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]
n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
cnt = 0
Q = deque

for i in range(n):
    for j in range(n):
        if board[i][j] == 1:
            board[i][j] = 0
            Q.append((i, j))
            while Q:                    # 주변에 1이 없으면 자동으로 끝남.
                tmp = Q.popleft()
                for k in range(8):
                    x = tmp[0] + dx[k]
                    y = tmp[1] + dy[k]
                    if 0 <= x < n and 0 <= y < n and board[x][y] == 1:
                        board[x][y] = 0
                        Q.append((x, y))
            cnt += 1
print(cnt)
