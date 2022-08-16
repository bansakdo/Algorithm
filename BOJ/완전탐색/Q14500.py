


N, M = map(int, input().split())
board = [list(map(int, input().split())) for i in range(N)]

# max_val = max(map(max, board))
# average = 0
tot = 0

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def explore(r, c, num_sum, cnt):
    global tot
    if cnt == 4:
        tot = max(num_sum, tot)
        return

    for i in range(4):
        nx = c + dx[i]
        ny = r + dy[i]

        if 0 <= nx < M and 0 <= ny < N and isVisit[ny][nx] == 0:
            # num_list.append(board[ny][nx])
            # isVisit[ny][nx] = 1
            # if len(num_list) == 3:
            #     explore(r, c, num_list, isVisit)
            # explore(ny, nx, num_list, isVisit)
            # num_list.pop()
            isVisit[ny][nx] = 1
            explore(ny, nx, num_sum + board[ny][nx], cnt + 1)
            isVisit[ny][nx] = 0

def f_shape(r, c):
    global tot
    for i in range(4):
        tmp = board[r][c]
        for j in range(3):
            k = (i + j) % 4
            ny = r + dy[k]
            nx = c + dx[k]

            if not (0 <= nx < M and 0 <= ny < N):
                tmp = 0
                break
            tmp += board[ny][nx]
        tot = max(tmp, tot)

isVisit = [[0] * M for _ in range(N)]
for r in range(N):
    for c in range(M):
        isVisit[r][c] = 1
        explore(r, c, board[r][c], 1)
        isVisit[r][c] = 0

        f_shape(r, c)

print(tot)





