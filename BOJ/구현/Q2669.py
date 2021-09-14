

squares = [list(map(int, input().split())) for _ in range(4)]   # 좌하단 x, y, 우상단 x, y

matrix = [[0 for _ in range(100)] for _ in range(100)]

for i in range(4):
    x1, y1, x2, y2 = squares[i]
    for row in range(y1, y2):
        for col in range(x1, x2):
            matrix[row][col] = 1

answer = sum([sum(matrix[row]) for row in range(100)])

print(answer)



'''
23
6 + 12 + 12 = 30
6 + 12 - 2 + 12 - 2 - 4 = 22



'''



