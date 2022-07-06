

T = int(input())

for _ in range(T):
    N = int(input())
    board = [list(map(int, list(input())))]
    board.append(list(input()))
    rst = board[1].count('*')
    d = [-1, 0, 1]

    for i in range(N):
        if board[1][i] != '*':
            continue
        for j in d:
            dx = i + j
            if 0 <= dx < N:
                board[0][dx] -= 1

    for i in range(N):
        if board[1][i] == '*':
            continue
        if board[0][i] > 0:
            board[1][i] = '*'

            idx = []
            for j in d:
                dx = i + j
                if 0 <= dx < N:
                    idx.append(dx)

            found = True
            for j in idx:
                board[0][j] -= 1
                if board[0][j] < 0:
                    found = False
            if not found:
                for j in idx:
                    board[0][j] += 1
                board[1][i] = '#'
    print(board[1].count('*'))


