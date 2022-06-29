
# 내가 푼거
'''
from collections import deque
from itertools import combinations

N, M = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(N)]
h_dist = [[[] for _ in range(N)] for _ in range(N)]

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

for r in range(N):
    for c in range(N):
        if city[r][c] != 1:
            continue
        visited = [[0] * N for _ in range(N)]
        visited[r][c] = 1
        queue = deque([[r, c]])

        while queue:
            row, col = queue.popleft()
            for d in range(4):
                nr = row + dy[d]
                nc = col + dx[d]
                if 0 <= nr < N and 0 <= nc < N and visited[nr][nc] == 0:
                    if city[nr][nc] == 2:
                        h_dist[r][c].append([nr, nc, abs(nr - r) + abs(nc - c)])
                    visited[nr][nc] = 1
                    queue.append([nr, nc])

chicken = [[r, c] for r in range(N) for c in range(N) if city[r][c] == 2]
home = [[r, c] for r in range(N) for c in range(N) if city[r][c] == 1]

min_dist = float('inf')
for i in range(M, 0, -1):
    c_comb = list(combinations(chicken, i))
    for comb in c_comb:
        dist = 0
        for hr, hc in home:
            tmp_dist = N ** 2
            for cr, cc, cd in h_dist[hr][hc]:
                if [cr, cc] in comb:
                    tmp_dist = min(tmp_dist, cd)
            dist += tmp_dist
        min_dist = min(min_dist, dist)

print(min_dist)
'''


# 다른사람이 푼거
from sys import stdin
from itertools import combinations

# stdin = open('./input.txt', 'r')
n, m = map(int, stdin.readline().split())
board = [list(map(int, stdin.readline().split())) for _ in range(n)]
homes = []
chickens = []
answer = int(1e9)

for i in range(n):
    for j in range(n):
        if board[i][j] == 1:
            homes.append((i, j))
        if board[i][j] == 2:
            chickens.append((i, j))

selected_chickens = list(combinations(chickens, len(chickens) - m))

def calcualte_chicken_distance(t):
    new_board = [[board[i][j] for j in range(n)] for i in range(n)]
    chikcen_sum = 0
    a = set(chickens)
    for k in t:
        new_board[k[0]][k[1]] = 0
        a.remove((k[0], k[1]))
    for home in homes:
        chicken_dist = int(1e9)
        for b in a:
            chicken_dist = min(chicken_dist, abs(home[0] - b[0]) + abs(home[1] - b[1]))
        chikcen_sum += chicken_dist
    return chikcen_sum


for selected_chicken in selected_chickens:
    answer = min(answer, calcualte_chicken_distance(selected_chicken))
print(answer)

