import sys
from collections import Counter

def check(r_s, r_e, c_s, c_e):
    global rst
    # if not reverse:
    #     __matrix = matrix
    # else
    #     __matrix = r_matrix
    for r in range(r_s, r_e + 1):
        row = matrix[r]
        rst = max(rst, max(Counter(row).values()))

    for r in range(r_s, r_e + 1):
        row = matrix[r]
        rst = max(rst, max(Counter(row).values()))


N = int(input())
matrix = list(input() for _ in range(N))
r_matrix = list(map(list, zip(*matrix)))
rst = 0

# print(list(Counter(matrix[0]).items()))

# for r in matrix:
#     if r.count(r[0]) == N:
#         print(N)
#         sys.exit()
# for r in r_matrix:
#     if r.count(r[0]) == N:
#         print(N)
#         sys.exit()

print(*r_matrix)

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

for x in range(N-1):
    for y in range(N-1):
        for i in range(4):
            n_x = x + dx[i]
            n_y = y + dy[i]
            if 0 <= n_x < N and 0 <= n_y < N and matrix[x][y] != matrix[n_x][n_y]:
                matrix[x][y], matrix[n_x][n_y] = matrix[n_x][n_y], matrix[x][y]
                # if i % 2 == 0:
                    










