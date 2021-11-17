
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def dfs(x, y):
    global M, N, K, ch, matrix

    ch[y][x] = 1
    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        if 0 <= nx < M and 0 <= ny < N and matrix[ny][nx] == 1 and ch[ny][nx] == 0:
            dfs(nx, ny)

def solution():
    global M, N, K, cnt, ch, matrix
    M, N, K = map(int, input().split())
    matrix = list([0 for _ in range(M)] for _ in range(N))
    ch = list([0 for _ in range(M)] for _ in range(N))
    cnt = 0
    if K > M * N - (min(M, N)):
        return 1

    for i in range(K):
        x, y = map(int, input().split())
        matrix[y][x] = 1
    for r in range(N):
        for c in range(M):
            if matrix[r][c] == 1 and ch[r][c] == 0:
                cnt += 1
                dfs(c, r)

    return cnt

if __name__ == "__main__":

    T = int(input())
    for _ in range(T):
        print(solution())
