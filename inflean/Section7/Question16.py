import sys

sys.stdin = open("input.txt", "rt")

# 16번 문제. 사다리 타리(DFS)

# 내 풀이
'''
dx = [0, 0, -1]
dy = [1, -1, 0]


def DFS(x, y):
    if x == 0:
        print(y)
        sys.exit(1)
    else:
        for i in range(3):
            xx = x + dx[i]
            yy = y + dy[i]
            if 0 <= xx < 10 and 0 <= yy < 10 and ch[xx][yy] == 0:
                ch[xx][yy] = 1
                if i != 2 and matrix[xx][yy] == 1:
                    DFS(xx, yy)
                    break
                elif i == 2:
                    DFS(xx, yy)


if __name__ == "__main__":
    matrix = [list(map(int, input().split())) for _ in range(10)]
    ch = [[0] * 10 for _ in range(10)]
    for i in range(10):
        if matrix[9][i] == 2:
            at = (9, i)
            break

    DFS(at[0], at[1])
'''


# 해설

def DFS(x, y):
    ch[x][y] = 1
    if x == 0:
        print(y)
    else:
        if y-1 >= 0 and board[x][y-1] == 1 and ch[x][y-1] == 0:
            DFS(x, y - 1)
        elif y+1 < 10 and board[x][y+1] == 1 and ch[x][y+1] == 0:
            DFS(x, y + 1)
        else:
            DFS(x - 1, y)

if __name__ == "__main__":
    board = [list(map(int, input().split())) for _ in range(10)]
    ch = [[0] * 10 for _ in range(10)]
    for y in range(10):
        if board[9][y] == 2:
            DFS(9, y)