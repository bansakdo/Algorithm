import sys
import copy
from collections import deque

sys.stdin = open("input.txt", "rt")
sys.setrecursionlimit(10 ** 6)

# 14번 문제. 안전영역 (BFS)

# 내 풀이
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
'''
n = int(input())
matrix = []
top = 0
maximum = 0
Q = deque()

for i in range(n):
    matrix.append(list(map(int, input().split())))
    if top < max(matrix[i]):
        top = max(matrix[i])

for k in range(1, top):
    mm = copy.deepcopy(matrix)
    cnt = 0
    for i in range(n):
        for j in range(n):
            if mm[i][j] > k:
                Q.append((i, j))
                mm[i][j] = 0
                cnt += 1
                while Q:
                    tmp = Q.popleft()
                    for l in range(4):
                        x = tmp[0] + dx[l]
                        y = tmp[1] + dy[l]
                        if 0 <= x < n and 0 <= y < n and mm[x][y] > k :
                            mm[x][y] = 0
                            Q.append((x, y))
    if cnt > maximum:
        maximum = cnt
print(maximum)
'''


# 해설
# DFS를 통해 풀이하는 방법.

def DFS(x, y, h):
    ch[x][y] = 1
    for i in range(4):
        xx = x + dx[i]
        yy = y + dy[i]
        if 0 <= xx < n and 0 <= yy < n and ch[xx][yy] == 0 and board[xx][yy] > h:
            DFS(xx, yy, h)


if __name__ == "__main__":
    n = int(input())
    cnt = 0
    res = 0
    board = [list(map(int, input().split())) for _ in range(n)]

    for h in range(100):
        ch = [[0] * n for _ in range(n)]
        cnt = 0
        for i in range(n):
            for j in range(n):
                if ch[i][j] == 0 and board[i][j] > h:
                    cnt += 1
                    DFS(i, j, h)
        res = max(res, cnt)
        if cnt == 0:
            break
print(res)