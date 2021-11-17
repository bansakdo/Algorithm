import sys

sys.stdin = open("input.txt", "rt")

# 17번 문제. 피자 배달 거리

# 내 풀이
'''
def Com(L, s):                  # 피자 m개 고르는 조합. numpCm
    if L == m:
        DFS()
    else:
        for i in range(s, nump):
            sp.append(p[i])
            Com(L + 1, i + 1)
            sp.pop()

def DFS():                      # 고른 피자집에서 배달거리 구함
    global minimum
    tot = 0
    # 한 집에서 가장 가까운 선택된 피자집과의 거리를 구해서 tot에 저장
    for i in range(numh):
        now = h[i]
        lowest = 2147000000
        for j in range(m):
            tmp = abs(sp[j][0] - now[0]) + abs(sp[j][1] - now[1])
            if tmp < lowest:
                lowest = tmp
        tot += lowest

    if minimum > tot:
        minimum = tot


if __name__ == "__main__":
    n, m = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(n)]
    h = []                  # 집
    p = []                  # 피자집
    sp = []                 #  선택된 피자집
    minimum = 2147000000

    for x in range(n):
        for y in range(n):
            if matrix[x][y] == 1:
                h.append((x, y))
            elif matrix[x][y] == 2:
                p.append((x, y))
    nump = len(p)
    numh = len(h)

    Com(0, 0)
    print(minimum)
'''

# 해설
def DFS(L, s):
    global res
    if L == m:
        sum = 0
        for j in range(len(hs)):
            x1 = hs[j][0]
            y1 = hs[j][1]
            dis = 2147000000
            for x in cb:
                x2 = pz[x][0]
                y2 = pz[x][1]
                dis = min(dis, abs(x1 - x2) + abs(y1-y2))
            sum += dis
        res = min(res, sum)
    else:
        for i in range(s, len(pz)):
            cb[L] = i
            DFS(L + 1, i + 1)


if __name__ == "__main__":
    n, m = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]
    hs = []         # 집
    pz = []         # 피자집
    cb = [0] * m    # 조합의 경우를 저장하는 리스트
    res = 2147000000

    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                hs.append((i, j))
            elif board[i][j] == 2:
                pz.append((i, j))
    DFS(0, 0)
    print(res)