

board = list(str(input()) for _ in range(10))
ch = list(list(0 for _ in range(10))for _ in range(10))

vertex = set()

dx = [0, 1, 1, 1, 0, -1, -1, -1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]

def discover(row, col, d):
    print(vertex)
    print(row, col, d)
    d_x = col + dx[d]
    d_y = row + dy[d]
    if 0 <= d_x < 10 and 0 <= d_y < 10 and board[d_y][d_x] == '1':
        # vertex.add(tuple([row, col]))
        return discover(d_y, d_x, d)
    else:
        return tuple([row, col])
    #     vertex.add(tuple([row, col]))



for row in range(10):
    for col in range(10):
        if ch[row][col] == 1:
            continue
        tmp = board[row][col]
        if board[row][col] == '1':
            for d in range(8):
                d_x = col + dx[d]
                d_y = row + dy[d]
                if 0 <= d_x < 10 and 0 <= d_y < 10 and board[d_y][d_x] == '1':
                    vertex.add(tuple([row, col]))
                    vertex.add(discover(d_y, d_x, d))
                if len(vertex) >= 3:
                    break
                else:
                    vertex.clear()




