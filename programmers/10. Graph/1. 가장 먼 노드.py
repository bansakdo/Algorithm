from collections import deque

def solution(n, edge):
    answer = 0
    edge = list(map(lambda x:(x[0], x[1]) if x[0] < x[1] else (x[1], x[0]), edge))
    print(edge)
    edge.sort(key=lambda x: (x[0], x[1]))
    print(edge)
    dic = {}
    for e in edge:
        tmp = dic.get(e[0], [])
        tmp.append(e[1])
        dic[e[0]] = tmp
    print(dic.items())
    distance = dict()
    # distance = []
    # for i in range(2, n+1):
    #     distance.append([i, 0])
    # print(distance)

    queue = deque([x, 1] for x in dic.get(1))
    while queue:
        node = queue.popleft()
        distance[node[0]] = node[1]
        next = dic[node[0]]
        for i in range(len(next)):
            queue.append([next[i], node[1] + 1])
    print(distance.items())



    return answer


n = 6
edge = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
print(solution(n, edge))




