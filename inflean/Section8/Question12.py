import sys
import copy

sys.stdin = open("input.txt", "rt")

# 12번 문제.  플로이드 워샬 알고리즘설
# 그래프에서 모든 정점에서 모든 정점으로 가는 최소값 구하기

# 내 풀이
'''
def DFS(origin, now, s):
    global res
    if res[origin][now] > s:
        res[origin][now] = s
    # if matrix[now]:
        # print(now)
    for i in range(n):
        # if matrix[now][i] != 0 and res[now][i] == 0:
        if matrix[now][i] != 0:
            # r = DFS(origin, i, s+matrix[now][i])
            # # if res[now][i] > r:
            # if r != 0:
            #     res[now][i] = min(res[now][i], r)
            #
            res[origin][i] = min(res[origin][i], s + matrix[now][i])


    return 0


n, m = map(int, input().split())
matrix = [[0] * n for _ in range(n)]

res = [[2147000000] * n for _ in range(n)]
for _ in range(m):
    a, b, c = map(int, input().split())
    matrix[a-1][b-1] = c
    res[a-1][b-1] = c
# res = copy.deepcopy(matrix)

for i in range(n):
    print(matrix[i])


for i in range(n):
    DFS(i, 0, 0)
# print(*res)
for i in range(n):
    for j in range(n):
        if i == j:
            res[i][j] = 0
            continue
        elif res[i][j] == 2147000000:
            res[i][j] = 'M'
print()
for i in range(n):
    print(res[i])
'''



# 해설

'''
각 점에서 모든 점으로 가는 최솟값 다 구한다.
'''

if __name__ == "__main__":
    n, m = map(int, input().split())
    dis = [[5000] * (n+1) for _ in range(n+1)]
    for i in range(n):
        dis[i][i] = 0

    # 경유하지 않고 한번에 갔을 때의 최소값
    for i in range(m):
        a, b, c = map(int, input().split())
        dis[a][b] = c

    # 플로이드 와샬 알고리즘. k를 거쳐서 i부터 j까지 갔을 때
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                dis[i][j] = min(dis[i][j], dis[i][k] + dis[k][j])

    for i in range(1, n+1):
        for j in range(1, n+1):
            if dis[i][j] == 5000:
                print("M", end=' ')
            else:
                print(dis[i][j], end=' ')
        print()