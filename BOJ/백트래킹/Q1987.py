
N, M = map(int, input().split())
graph = [list(input()) for _ in range(N)]
board = [[False for _ in range(M)] for _ in range(N)]
dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]

result = 0


def dfs(r, c, visit, alphabet):
    global result
    count = 0
    alphabet_set = set(visit)
    if board[r][c] != alphabet_set:
        board[r][c] = alphabet_set
        visit.append(graph[r][c])
        for i in range(4):
            new_r = r + dy[i]
            new_c = c + dx[i]
            if 0 <= new_r < N and 0 <= new_c < M and graph[new_r][new_c] not in visit:
                count += 1
                li = visit[:]
                dfs(new_r, new_c, li, alphabet + 1)
    if count == 0:
        result = max(result, alphabet)


dfs(0, 0, [], 1)
print(result)