import sys

sys.stdin = open("input.txt", "rt")

# 15번 문제. 경로탐색 (그래프 DFS)

# 내 풀이
# '''
def DFS(L):
    global cnt, ch, res
    if res[-1] == n:
        # print("res:", res)
        cnt += 1
        return
    else:
        r = res[-1]                             # row
        for c, v in enumerate(matrix[r]):       # column, value
            if v == 1 and ch[c] == 0:
                # print(L, r, c, v)
                ch[c] = 1
                res.append(c)
                DFS(L + 1)
                ch[c] = 0
                res.pop()

if __name__ == "__main__":
    n, m = map(int, input().split())
    matrix = [[0]*(n+1) for _ in range(n + 1)]          # n*n 배열
    ch = [0] * (n + 1)                                  # 현재 배열에 해당 노드 포함 여부.
    ch[1] = 1
    res = [1]                                           # 경로 담을 리스트
    cnt = 0                                             # 경우의 수
    for _ in range(m):                                  # 배열에 경로 값 대입
        r, c = map(int, input().split())
        matrix[r][c] = 1

    for i in range(1, n + 1):                           # 배열 출력
        for j in range(1, n + 1):
            print(matrix[i][j], end=' ')
        print()

    DFS(1)
    print(cnt)
# '''


# 해설
'''
한번 방문한 노드는 다시 방문하지 않도록 체크리스트 필요.
방문 후 다시 돌아갈 때에는 체크 풀기 
'''
'''
def DFS(v):         # v: 노드 번호
    global cnt
    if v == n:
        print(path)
        cnt += 1
    else:
        for i in range(1, n + 1):
            if g[v][i] == 1 and ch[i] == 0:
                ch[i] = 1
                path.append(i)
                DFS(i)
                path.pop()
                ch[i] = 0


if __name__ == "__main__":
    n, m = map(int, input().split())
    g = [[0] * (n + 1) for _ in range(n+1)]
    ch = [0] * (n + 1)
    for i in range(m):
        a, b = map(int, input().split())
        g[a][b] = 1
    cnt = 0
    path = []
    path.append(1)
    ch[1] = 1
    DFS(1)
    print(cnt)
'''