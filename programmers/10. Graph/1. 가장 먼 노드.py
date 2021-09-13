from collections import deque


def solution(n, edge):

    graph = dict()
    for n1, n2 in edge:
        if n1 in graph:
            node1 = graph.get(n1)
            node1.add(n2)
            graph[n1] = node1
        else:
            graph[n1] = {n2}
        if n2 in graph:
            node2 = graph.get(n2)
            node2.add(n1)
            graph[n2] = node2
        else:
            graph[n2] = {n1}

    distance = dict()
    check = [0 for _ in range(n+1)]
    check[1] = 1
    queue = deque([node, 1] for node in list(graph.get(1)))
    while queue:
        node, cnt = queue.popleft()
        if check[node] == 1:
            distance[node] = min(cnt, distance.get(node))
            continue

        check[node] = 1
        distance[node] = cnt
        for next_node in list(graph.get(node)):
            if check[next_node] == 0:
                queue.append([next_node, cnt+1])

    distance = list(distance.values())
    answer = distance.count(max(distance))

    return answer


n = 6
edge = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
# n = 10
# edge = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2], [6, 7], [4, 6], [4, 8], [5, 9], [5, 10], [4, 9], [6, 7]]
print(solution(n, edge))




