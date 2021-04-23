import sys
from collections import deque
import heapq as hq

sys.stdin = open("input.txt", "rt")

# 10번 문제. 최소 힙

queue = deque()
'''
while True:
    x = int(input())
    if x == -1:
        break
    elif x == 0:
        print(queue )
        print(queue[0])
        queue.clear()
    else:
        for i in range(len(queue)):
            if i == 0 and x < queue[0]:
                queue.appendleft(x)
                break
            elif queue[i] > x:
                queue.insert(i + 1, x)
                break
        else:
            queue.append(x)
'''

# 해설
a = []
while True:
    n = int(input())
    if n == -1:
        break
    if n == 0:
        if len(a) == 0:
            print(-1)
        else:
            print(hq.heappop(a))        # heap에서 루트로드를 pop함
    else:
        hq.heappush(a, n)               # a리스트에 n 값을 최소힙의 형태로 푸시