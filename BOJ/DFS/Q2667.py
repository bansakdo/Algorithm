

# 상 우 하 좌
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def dfs(x, y):
    global N
    ch[x][y] = 1
    tot = 1
    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        if 0 <= nx < N and 0 <= ny < N and matrix[nx][ny] == '1' and ch[nx][ny] == 0:
            tot += dfs(nx, ny)
    return tot


if __name__ == "__main__":
    N = int(input())
    village = []
    matrix = [str(input()) for _ in range(N)]
    ch = [[0 for _ in range(N)] for _ in range(N)]

    for x in range(N):
        for y in range(N):
            if matrix[x][y] == '1' and ch[x][y] == 0:
                village.append(dfs(x, y))

    print(len(village))
    print(*sorted(village), sep='\n')
