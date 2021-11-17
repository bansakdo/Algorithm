import sys

# DFS 사용한 방법
'''
# recursion error 떠서 recursion limit 늘려줌
sys.setrecursionlimit(10 ** 9)

def DFS(start):
    for i in Tree[start]:
        if Parent[i] == 0:
            Parent[i] = start
            DFS(i)

n = int(sys.stdin.readline())

Tree = list(list() for _ in range(n+1))
Parent = list(0 for _ in range(n+1))

for _ in range(n-1):
    a, b = map(int, sys.stdin.readline().split())
    Tree[a].append(b)
    Tree[b].append(a)

Parent[1] = -1
DFS(1)

for x in Parent[2:]:
    print(x)
'''


# BFS

from collections import deque

n = int(sys.stdin.readline())
Tree = list(list() for _ in range(n+1))
Parent = list(0 for _ in range(n+1))

for _ in range(n-1):
    a, b = map(int, sys.stdin.readline().split())
    Tree[a].append(b)
    Tree[b].append(a)

queue = deque([1])

while queue:
    tmp = queue.popleft()
    for i in Tree[tmp]:
        if Parent[i] == 0:
            Parent[i] = tmp
            queue.append(i)


for x in Parent[2:]:
    print(x)




'''
18
1 2
1 3
2 4
3 5
3 6
4 7
4 8
5 9
5 10
6 11
6 12
7 13
8 14
10 15
10 16
12 17
12 18

=>
1
1
2
3
3
4
4
5
5
6
6
7
8
10
10
12
12

'''