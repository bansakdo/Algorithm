from collections import deque


def dfs(node):
    global edges, ch, rst_dfs
    ch[node] = 1
    rst_dfs.append(node)
    edge = sorted(edges[node])
    for e in edge:
        if ch[e] == 0:
            dfs(e)


if __name__ == "__main__":
    N, M, V = map(int, input().split())
    edges = [[] for _ in range(N + 1)]
    for _ in range(M):
        n1, n2 = map(int, input().split())
        edges[n1].append(n2)
        edges[n2].append(n1)

    # dfs
    ch = [0 for _ in range(N + 1)]
    rst_dfs = []
    dfs(V)

    # bfs
    rst_bfs = []
    queue = deque([V])
    while queue:
        node = queue.popleft()
        rst_bfs.append(node)
        edge = sorted(edges[node])
        for e in edge:
            if e not in rst_bfs and e not in queue:
                queue.append(e)

    print(*rst_dfs)
    print(*rst_bfs)
