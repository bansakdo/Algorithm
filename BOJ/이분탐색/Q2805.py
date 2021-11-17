import sys
import time
'''
INPUT
4 7
20 15 10 17
'''


# sys.stdin = open("Q2805.txt", "rt")
start = time.time()

# 2805번. 나무자르기
'''
n, m = map(int, input().split())
tree = list(map(int, input().split()))

a = 0
b = max(tree)
# b = 2147000000

# for x in tree:
#     if x > a:
#         a = x
#     if x < b:
#         b = x
print(a, b)

mid = (b + a) // 2
res = 0
while a < b:
    tot = 0
    mid = (a + b) // 2
    for x in tree:
        # if x - mid <= 0:
        #     continue
        # else:
        if x - mid >= 0:
            tot += (x - mid)
    print(a, b, mid, tot)
    # if tot == m:
    #     print(mid)
    #     break
    if tot >= m:                # 너무 많이 자름
        # mid = (b + mid) // 2
        a = mid + 1
    elif tot < m:               # 적게 자름
        # mid = (mid + a) // 2 + a
        b = mid - 1
print(mid)
'''
input = sys.stdin.readline
# '''
n, m = map(int, input().split())
tree = list(map(int, input().split()))
a = 1
b = max(tree)

res = 0
while a <= b:
    tot = 0
    mid = (a + b) // 2
    for x in tree:
        if x - mid >= 0:
            tot += (x - mid)
    print(a, b, mid, tot)
    # if tot == m:
    #     print(mid)
    #     break
    if tot >= m:
        a = mid + 1
        res = mid
    elif tot < m:
        b = mid - 1
print(res)
# '''
'''
N, M = map(int, input().split())
tree = list(map(int, input().split()))
start, end = 1, max(tree)  # 이분탐색 검색 범위 설정

while start <= end:  # 적절한 벌목 높이를 찾는 알고리즘
    mid = (start + end) // 2

    log = 0  # 벌목된 나무 총합
    for i in tree:
        if i >= mid:
            log += i - mid
    print(start, end, mid, log)
    # 벌목 높이를 이분탐색
    if log >= M:
        start = mid + 1
    else:
        end = mid - 1
print(end)
'''
print("time :", time.time() - start)