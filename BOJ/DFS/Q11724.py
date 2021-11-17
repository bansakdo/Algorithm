import sys


# DFS
# '''
sys.setrecursionlimit(10**5)

def DFS(node):
    ch[node] = 1
    edge = edges[node]
    while edge:
        next = edge.pop()
        if ch[next] == 0:
            DFS(next)


if __name__ == "__main__":

    n, m = map(int, sys.stdin.readline().split())
    graph = 0
    edges = [[] for _ in range(n+1)]
    ch = [0] * (n + 1)

    for _ in range(m):
        a, b = map(int, sys.stdin.readline().split())
        edges[a].append(b)
        edges[b].append(a)

    for i in range(1, n + 1):
        if ch[i] == 0:
            graph += 1
            DFS(i)

    print(graph)
# '''

