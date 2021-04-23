import sys
from collections import deque


sys.stdin = open("input.txt", "rt")


# 9번 문제. 미로의 최단겨리 통로 (BFS 활용)
'''
def DFS(L, r, c):
    # print()
    # print(L, r, c)
    # print(path)
    global cnt
    if r == 6 and c == 6:
        if L < cnt:
            cnt = L
    elif L > cnt:
        return
    else:
        path.append([r, c])
        if r > 0 and matrix[r - 1][c] == 0 and not [r - 1, c] in path:         # 상
            DFS(L + 1, r - 1, c)
        if r < 6 and matrix[r + 1][c] == 0 and not [r + 1, c] in path:         # 하
            DFS(L + 1, r + 1, c)
        if c > 0 and matrix[r][c - 1] == 0 and not [r, c - 1] in path:         # 좌
            DFS(L + 1, r, c - 1)
        if c < 6 and matrix[r][c + 1] == 0 and not [r, c + 1] in path:         # 우
            DFS(L + 1, r, c + 1)
        path.pop()


if __name__ == "__main__":
    matrix = []
    for _ in range(7):
        matrix.append(list(map(int, input().split())))
    cnt = 2147000000
    path = []


    DFS(0, 0, 0)
    if cnt == 2147000000:
        print("-1")
    else:
        print(cnt)
'''


# 해설
'''
최단거리 문제는 BFS로 푼다.
'''

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
board = [list(map(int, input().split())) for _ in range(7)]
dis = [[0] * 7 for _ in range(7)]                               # 거리 저장
Q = deque()                                                     # 이전 좌표들
Q.append((0, 0))
board[0][0] = 1

while Q:
    tmp = Q.popleft()
    for i in range(4):                                          # 상하좌우 네번 반복
        x = tmp[0] + dx[i]
        y = tmp[1] + dy[i]
        if 0 <= x <= 6 and 0 <= y <= 6 and board[x][y] == 0:
            board[x][y] = 1                                     # 지나온 곳은 벽으로 처리
            dis[x][y] = dis[tmp[0]][tmp[1]] + 1                 # 이전 칸 + 1
            Q.append((x, y))
if dis[6][6] == 0:
    print(-1)
else:
    print(dis[6][6])




