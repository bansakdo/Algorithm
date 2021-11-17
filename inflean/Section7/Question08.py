import sys
from collections import deque

sys.stdin = open("input.txt", "rt")
# 8번 문제. 사과나무 (BFS)


# 내 풀이
'''
def DFS(L, s, e):
    global tot
    if L == n:
        print(tot)
        return
    else:
        tot += sum(matrix[L][s:e])
        if L < center:
            DFS(L + 1, s - 1, e + 1)
        else:
            DFS(L + 1, s + 1, e - 1)

if __name__ == "__main__":
    n = int(input())
    matrix = []
    for _ in range(n):
        matrix.append(list(map(int, input().split())))
    tot = 0
    center = n // 2

    DFS(0, center, center + 1)
'''

# 해설
'''
BFS를 통해 푸는 방법. 
정 중앙에서 시작하여 상하좌우 탐색.
이미 지나온 곳을 다시 가지 않도록 지나온 좌표를 따로 저장.
상하좌우 뻗어나간 뒤에 다시 상하좌우 반복. 따라서 한 부모 노드 당 4개의 자식노드 생성.
'''

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
ch = [[0] * n for _ in range(n)]
sum = 0
Q = deque()
ch[n//2][n//2] = 1
Q.append((n//2, n//2))
L = 0

while True:
    if L == n // 2:
        break
    size = len(Q)                   # 바로 직전에 탐색된 나무들의 수
    for i in range(size):
        tmp = Q.popleft()
        for j in range(4):
            x = tmp[0] + dx[j]
            y = tmp[1] + dy[j]
            if ch[x][y] == 0:
                sum += a[x][y]
                ch[x][y] = 1
                Q.append((x, y))
    L += 1



