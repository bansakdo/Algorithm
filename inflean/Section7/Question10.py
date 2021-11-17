import sys

sys.stdin = open("input.txt", "rt")


# 10번 문제. 미로 탐색 (DFS)

# 내 풀이
'''
def DFS(y, x):
    global cnt
    if x == y == 6:
        cnt += 1
        return
    else:
        for k in range(4):
            next_x = x + dx[k]
            next_y = y + dy[k]
            if 0 <= next_x <= 6 and 0 <= next_y <= 6 and matrix[next_y][next_x] == 0 and ch[next_y][next_x] == 0:
                ch[next_y][next_x] = 1
                DFS(next_y, next_x)
                ch[next_y][next_x] = 0


if __name__ == "__main__":
    matrix = [list(map(int, input().split())) for _ in range(7)]
    ch = [[0] * 7 for _ in range(7)]
    ch[0][0] = 1
    dx = [0, -1, 0, 1]          # 하, 좌, 상, 우
    dy = [1, 0, -1, 0]
    cnt = 0

    DFS(0, 0)
    print(cnt)
'''



# 해설
'''
BFS는 정 중앙에서 다방향으로 천천히 뻗어나간다면, 
DFS는 한 방향으로 끝까지 갔다가 막히면 다시 돌아와 다른방향으로 가는것을 반복.

이 문제는 DFS로 해결.
'''

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def DFS(x, y):
    global cnt
    if x == 6 and y == 6:
        cnt += 1
    else:
        for i in range(4):
            xx = x + dx[i]
            yy = y + dx[i]
            if 0 <= xx <= 6 and 0 <= yy <= 6 and board[xx][yy] == 0:
                board[xx][yy] = 1
                DFS(xx, yy)
                board[xx][yy] = 0



if __name__ == "__main__":
    board = [list(map(int, input().split())) for _ in range(7)]
    cnt = 0
    board[0][0] = 1
    DFS(0, 0)
    print(cnt)


