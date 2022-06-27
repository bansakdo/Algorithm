from collections import deque


N = int(input())
board = [list(map(int, list(input()))) for _ in range(N)]
convert = 0
b_rooms = [[0 for _ in range(N)] for _ in range(N)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

for i in range(N * N):
    queue = deque([[0, 0]])
    c_board = [r.copy() for r in board]
    b_rooms = [[0 for _ in range(N)] for _ in range(N)]
    b_rooms[0][0] = i


# 내가 푼 방법
'''
    while queue:
        x, y = queue.popleft()
        c = b_rooms[x][y]
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if nx == ny == N - 1:
                print(i)
                exit()

            if 0 <= nx < N and 0 <= ny < N:
                if c_board[nx][ny] == 1:
                    c_board[nx][ny] = 2
                    b_rooms[nx][ny] = max(b_rooms[nx][ny], c)
                    queue.append([nx, ny])
                elif c_board[nx][ny] == 0 and c > 0:
                    c_board[nx][ny] = 2
                    b_rooms[nx][ny] = max(b_rooms[nx][ny], c - 1)
                    queue.append([nx, ny])
                elif c_board[nx][ny] == 2:
                    flag = False
                    if board[nx][ny] == 1 and b_rooms[nx][ny] < c:
                        b_rooms[nx][ny] = c
                        flag = True
                    elif board[nx][ny] == 0 and b_rooms[nx][ny] < c - 1:
                        b_rooms[nx][ny] = c - 1
                        flag = True

                    if flag:
                        for q in queue:
                            if q == [nx, ny]:
                                break
                        else:
                            queue.append([nx, ny])
'''

# BFS
'''
ch = [[-1] * N for i in range(N)]
while queue:
    x, y = queue.popleft()

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < N and 0 <= ny < N:
            if ch[nx][ny] == -1:
                if board[nx][ny] == 0:
                    ch[nx][ny] = ch[x][y] + 1
                    queue.append([nx, ny])
                else:
                    ch[nx][ny] = ch[x][y]
                    queue.appendleft([nx, ny])
'''

# 다익스트라

import heapq

visited = [[0] * N for _ in range(N)]

heap = []
heapq.heappush(heap, [0, 0, 0])
visited[0][0] = 1
while heap:
    cost, x, y = heapq.heappop(heap)
    if x == N - 1 and y == N - 1:
        print(cost)
        exit()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
            visited[nx][ny] = True
            if board[nx][ny] == 0:
                heapq.heappush(heap, [cost + 1, nx, ny])
            else:
                heapq.heappush(heap, [cost, nx, ny])

