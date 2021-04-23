import sys

sys.stdin = open("input.txt", "rt")

# 11번 문제. 등산경로 (DFS)

# 내 풀이
'''
def DFS(r, c):
    global cnt
    if r == highest[0] and c == highest[1]:
        cnt += 1
    else:
        cur = matrix[r][c]
        for i in range(4):
            next_row = r + dy[i]
            next_column = c + dx[i]
            if 0 <= next_row < n and 0 <= next_column < n and matrix[next_row][next_column] > cur:
                DFS(next_row, next_column)


if __name__ == "__main__":
    n = int(input())
    matrix = []
    lowest = [-1, -1, 2147000000]
    highest = [-1, -1, -2147000000]
    for i in range(n):
        tmp = list(map(int, input().split()))
        l = min(tmp)
        h = max(tmp)
        if lowest[2] > l:
            lowest = [i, tmp.index(l), l]
        if highest[2] < h:
            highest = [i, tmp.index(h), h]
        matrix.append(tmp)
    cnt = 0
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]

    # for i in range(n):
    #     print(matrix[i])
    # print(lowest)
    # print(highest)
    DFS(lowest[0], lowest[1])
    print(cnt)
'''


# 해설

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def DFS(x, y):
    global cnt
    if x == ex and y == ey:
        cnt += 1
    else:
        for k in range(4):
            xx = x + dx[k]
            yy = y + dy[k]
            if 0 <= xx < n and 0 <= yy < n and ch[xx][yy] == 0 and board[xx][yy] > board[x][y]:
                ch[xx][yy] = 1
                DFS(xx, yy)
                ch[xx][yy] = 0

if __name__ == "__main__":
    n = int(input())
    board = [[0] * n for _ in range(n)]
    ch = [[0] * n for _ in range(n)]
    max = -2147000000
    min = 2147000000
    for i in range(n):
        tmp = list(map(int, input().split()))
        for j in range(n):
            if tmp[j] < min:
                min = tmp[j]
                sx = i              # 시작점 x
                sy = j              # 시작점 y
            if tmp[j] > max:
                amx = tmp[j]
                ex = i              # 도착점 x
                ey = j              # 도착점 y
            board[i][j] = tmp[j]
    ch[sx][sy] = 1
    cnt = 0
    DFS(sx, sy)
    print(cnt)


