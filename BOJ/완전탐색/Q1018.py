

N, M = map(int, input().split())
board = [[True if x == 'B' else False for x in list(input())] for _ in range(N)]
draw_board = [[0 for _ in range(M)] for _ in range(N)]

for row in range(N):
    for col in range(M):
        if row == col == 0:
            continue
        elif col == 0:
            if board[row][col] == board[row - 1][col]:
                board[row][col] = not board[row - 1][col]
                draw_board[row][col] = 1
        else:
            if board[row][col] == board[row][col - 1]:
                board[row][col] = not board[row][col - 1]
                draw_board[row][col] = 1

num = 64
for row in range(N - 7):
    for col in range(M - 7):
        tot = sum([sum(draw_board[r][col:col+8]) for r in range(row, row + 8)])
        num = min(num, 64 - tot, tot)

print(num)
