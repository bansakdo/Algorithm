from collections import deque

N, M = map(int, input().split())

ladders = [list(map(int, input().split())) for _ in range(N)]
snakes = [list(map(int, input().split())) for _ in range(M)]

ls = dict()
for i in range(N):
    ls[ladders[i][0]] = [1, ladders[i][1]]
for i in range(M):
    ls[snakes[i][0]] = [2, snakes[i][1]]

queue = deque([1])
board = [0] * 100

while queue:
    pos = queue.popleft()
    cnt = board[pos]

    for i in range(1, 7):
        next_pos = pos + i
        if next_pos > 100:
            continue
        if next_pos == 100:
            print(cnt + 1)
            queue.clear()
            break

        if next_pos in ls.keys():
            next_pos = ls[next_pos][1]
        if board[next_pos] != 0:
            continue
        board[pos + i] = cnt + 1
        board[next_pos] = cnt + 1
        queue.append(next_pos)

