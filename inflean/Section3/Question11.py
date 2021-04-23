import sys

sys.stdin = open("input.txt", "rt")

# 11번 문제. 격자판 회문수

# 내가 푼거
'''
matrix = [list(map(int, input().split())) for _ in range(7)]
cnt = 0
# 행
for i in range(7):
    for j in range(2, 5):
        if (matrix[i][j - 1] == matrix[i][j + 1]) and (matrix[i][j - 2] == matrix[i][j + 2]):
            cnt += 1
# 열
for i in range(7):
    for j in range(2, 5):
        if (matrix[j - 1][i] == matrix[j + 1][i]) and (matrix[j - 2][i] == matrix[j + 2][i]):
            cnt += 1

print(cnt)
'''

# 해설

board = [list(map(int, input().split())) for _ in range(7)]
cnt = 0
for i in range(3):
    for j in range(7):
        tmp = board[j][i:i+5]
        if tmp == tmp[::-1]:
            cnt += 1
        for k in range(2):
            if board[i+k][j] != board[i+5-k-1][j]:
                break
        else:
            cnt += 1

