
from collections import deque


def check(num):
    visited[num] = True
    stack = deque([num])

    while stack:
        node = stack.popleft()
        for n_node in trees[node]:                  # bfs
            if trees[node][n_node] == 0:            # 엣지 체크 (0: 체크 안함, 1: 체크함)
                if not visited[n_node]:             # 해당 노드에 처음 방문
                    visited[n_node] = True
                    stack.append(n_node)            # 대기열에 다음 노드 추가
                    trees[node][n_node] = 1
                    trees[n_node][node] = 1
                else:
                    return False                    # 헤당 노드에 방문한 적이 있으므로 그래프
    return True



test = 0
while True:
    test += 1
    N, M = map(int, input().split())
    if N == 0 and M == 0:
        break
    edges = [list(map(int, input().split())) for _ in range(M)]
    visited = [False] * (N + 1)
    trees = [{} for _ in range(N+1)]
    for e in edges:
        trees[e[0]][e[1]] = 0           # 엣지 체크. 0: 체크X, 1: 체크 O
        trees[e[1]][e[0]] = 0

    cnt = 0
    for num in range(1, N + 1):
        if not visited[num]:
            if check(num):
                cnt += 1

    print("Case {}: ".format(test), end="")
    if cnt == 0:
        print("No trees.")
    elif cnt == 1:
        print("There is one tree.")
    else:
        print("A forest of {} trees.".format(cnt))


