import sys
from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

R, C = map(int, input().split())
matrix = list()

water = deque()
D = deque()
S = deque()

turn = 0

for i in range(R):
    tmp = input()
    matrix.append(tmp)
    if '*' in tmp:
        water.append([i, tmp.index('*')])
    if 'D' in tmp:
        D.append([i, tmp.index('D')])
    if 'S' in tmp:
        S.append([i, tmp.index('S')])


while S:
    turn += 1

    next_S = []
    while S:
        s_now = S.popleft()
        if matrix[s_now[0]][s_now[1]] != 'S':
            continue
        for i in range(4):
            s_next = [s_now[0] + dx[i], s_now[1] + dy[i]]
            if 0 <= s_next[0] < R and 0 <= s_next[1] < C and matrix[s_next[0]][s_next[1]] not in ['*', 'X']:
                if matrix[s_next[0]][s_next[1]] == 'D':
                    print(turn)
                    sys.exit()
                matrix[s_next[0]] = matrix[s_next[0]][:s_next[1]] + 'S' + matrix[s_next[0]][s_next[1] + 1:]
                next_S.append(s_next)
        else:
            matrix[s_now[0]] = matrix[s_now[0]][:s_now[1]] + '.' + matrix[s_now[0]][s_now[1] + 1:]
    S = deque(next_S)

    next_water = []
    while water:
        w_now = water.popleft()
        for i in range(4):
            w_next = [w_now[0] + dx[i], w_now[1] + dy[i]]
            if 0 <= w_next[0] < R and 0 <= w_next[1] < C and matrix[w_next[0]][w_next[1]] in ['.', 'S']:
                matrix[w_next[0]] = matrix[w_next[0]][:w_next[1]] + '*' + matrix[w_next[0]][w_next[1] + 1:]
                next_water.append(w_next)
    water = deque(next_water)

print("KAKTUS")





