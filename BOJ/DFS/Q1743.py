import sys
sys.setrecursionlimit(10**4)

# 하 좌 상 우
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]


def dfs(x, y):
    global ch_matrix, matrix
    ch_matrix[x][y] = 1
    cnt = 1

    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        if 0 <= nx < N and 0 <= ny < M and matrix[nx][ny] == '#' and ch_matrix[nx][ny] == 0:
            ch_matrix[nx][ny] = 1
            cnt += dfs(nx, ny)
    return cnt


N, M, K = map(int, input().split())
garbage = [tuple(map(int, input().split())) for _ in range(K)]
matrix = []
for _ in range(N):
    matrix.append(['.' for _ in range(M)])
for x, y in garbage:
    matrix[x-1][y-1] = '#'
largest = 0
ch_matrix = []
for _ in range(N):
    ch_matrix.append([0 for _ in range(M)])

for x in range(N):
    for y in range(M):
        if matrix[x][y] == '#' and ch_matrix[x][y] == 0:
            ch_matrix[x][y] = 1
            largest = max(largest, dfs(x, y))

print(largest)