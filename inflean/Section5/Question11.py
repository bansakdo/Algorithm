import sys
import heapq as hq

sys.stdin = open("input.txt", "rt")

# 11번 문제. 최대힙

# 내 풀이 (실패)
'''
a = []
while True:
    n = int(input())
    if n == -1:
        break
    elif n == 0:
        if len(a) == 0:
            print(-1)
        else:
            print(hq.heappop(a))
            a.clear()
'''

# 해설
a = []
while True:
    n = int(input())
    if n == -1:
        break
    elif n == 0:
        if len(a) == 0:
            print(-1)
        else:
            print(-hq.heappop(a))
    else:
        hq.heappush(a, -n)

