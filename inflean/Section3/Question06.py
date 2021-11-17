import sys

sys.stdin = open("input.txt", "rt")

# 6번 문제. 격자판 최대합

# 내가 푼거
'''
n = int(input())

matrix = [[int(x) for x in input().split()] for _ in range(n)]
max_val = 0
# 행의 합
for i in range(n):
    sumRow = sum(matrix[i])
    if sumRow > max_val:
        max_val = sumRow
# 열의 합
for i in range(n):
    sumCol = sum([matrix[j][i] for j in range(n)])
    if sumCol > max_val:
        max_val = sumCol
# 대각선의 합
diagonal1 = sum([matrix[x][x] for x in range(n)])
if diagonal1 > max_val:
    max_val = diagonal1
diagonal2 = sum([matrix[x][n - x - 1] for x in range(n)])
if diagonal2 > max_val:
    max_val = diagonal2
print(max_val)
'''

# 해설

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
tot = -2147000000
for i in range(n):
    sum1 = sum2 = 0
    for j in range(n):
        sum1 += a[i][j]             # 행의 합
        sum2 += a[j][i]             # 열의 합
    if sum1 > tot:
        tot = sum1
    if sum2 > tot:
        tot = sum2
sum1 = sum2 = 0
for i in range(n):
    sum1 += a[i][i]
    sum2 += a[i][n - i - 1]
    if sum1 > tot:
        tot = sum1
    if sum2 > tot:
        tot = sum2
print(tot)
