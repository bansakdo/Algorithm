

# 1715 문제. 카드 정렬하기
'''
INPUT
3
40
20
10
'''

import heapq

'''
n = int(input())
c = []
for _ in range(n):
    c.append(int(input()))

# for i in range(n):
#     for j in range(n - i - 1):
#         if c[j] > c[j+1]:
#             c[j], c[j+1] = c[j+1], c[j]
# c.sort()
res = c[0] / 2
del c[0]
while c:
    res = res * 2
    res += c[0]
    del c[0]

print(int(res))
'''


import heapq

n = int(input())
c = []
for _ in range(n):
    c.append(int(input()))

heapq.heapify(c)
res = 0
while len(c) > 1:
    a = heapq.heappop(c)
    b = heapq.heappop(c)
    res += a+b
    heapq.heappush(c, a+b)

print(res)



