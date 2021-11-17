import sys


sys.stdin = open("input.txt", "rt")


# 14번 문제. 인접행렬 (가중치 방향그래프)
'''
if __name__ == "__main__":
    n, m = map(int, input().split())
    matrix = [[0]*n for _ in range(n)]      # NxN 2차 리스트 생성

    for _ in range(m):
        r, c, v = map(int, input().split())     # row, column, value
        matrix[r-1][c-1] = v

    for x in matrix:
        print(x)
'''


# 해설

n, m = map(int, input().split())
g = [[0]*(n+1) for _ in range(n+1)]
for i in range(m):
    a, b, c = map(int, input().split())
    g[a][b] = c

for i in range(1, n+1):
    for j in range(1, n+1):
        print(g[i][j], end=' ')
    print()