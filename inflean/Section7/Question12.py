import sys

sys.stdin = open("input.txt", "rt")

# 12번 문제. 단지 번호 붙이기(DFS, BFS)


# 내 풀이
'''
def DFS(r, c, L):
    print(r, c, matrix[r][c])
    if r == c == 6:
        return
        # return
    else:
        if matrix[r][c] == '0':
            ch[r][c] = 0
            print("==")
        else:
            # if matrix[r][c] != 0:
            # ch[r][c] = L
            # print(r, c, L)
            # res.append(L)
        for i in range(4):
            next_r = r + dy[i]
            next_c = c + dx[i]
            if
            if 0 <= next_r < n and 0 <= next_c < n and ch[next_r][next_c] == -1:
                # if matrix[next_r][next_c] == 0:
                #     ch[next_r][next_c] = 0
                # else:
                    # ch[]
                DFS(next_r, next_c, L)



if __name__ == "__main__":
    n = int(input())
    matrix = [str(input()) for _ in range(n)]
    print(matrix)
    ch = [[-1] * n for _ in range(n)]
    # if matrix[0][0]
    ch[0][0] = 0
    res = []
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]

    DFS(0, 0, 1)
    print(res)
'''



# 해설
'''
0행부터 시작. 원소를 탐색하며 원소가 1이 발견되면 DFS 시작. 체크 된 것은 1을 0으로 변환.
하나의 DFS가 끝나면 res에 아파스 수를 append 하고, 한 단지 생성됨.
그리고 원래 탐색하던 행에서 다시 원소 탐색 시작.
입력값에 한 줄에 띄어쓰기가 안되어 있으므로 입력받을 때 split 사용 X
'''

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def DFS(x, y):
    global cnt
    cnt += 1
    board[x][y] = 0                 # 현재 위치를 다시 방문하지 않기 위해서 0으로 만듦.
    for i in range(4):
        xx = x + dx[i]
        yy = y + dy[i]
        if 0 <= xx < n and 0 <= yy < n and board[xx][yy] == 1:
            DFS(xx, yy)


if __name__ =="__main__":
    n = int(input())
    board = [list(map(int, input())) for _ in range(n)]         # 숫자를 읽어서 list화.
    res = []

    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                cnt = 0
                DFS(i, j)
                res.append(cnt)
    print(len(res))
    res.sort()
    for x in res:
        print(x)

