import sys

sys.stdin = open("input.txt", "rt")

# 5번 문제. 정다면체

# 내가 푼거
'''
n, m = map(int, input().split())

arr_n = [int(x) for x in range(1, n+1)]
arr_m = [int(x) for x in range(1, m+1)]
val = {}                                # 딕셔너리 선언
for i in range(n):
    for j in range(m):
        tmp = arr_n[i]+arr_m[j]
        if tmp in val:
            val[tmp] = val[tmp]+1
        else:
            val[tmp] = 1

max_val = 0
res = list()
for key in val.keys():
    if max_val < val[key]:
        max_val = val[key]
        res.clear()
        res.append(key)
    elif max_val == val[key]:
        res.append(key)
for i in res:
    print(i, end=' ')
'''
# 방법 2. 해설에서 처음에 알려준 방법
'''
n, m = map(int, input().split())

arr_n = [int(x) for x in range(1, n+1)]
arr_m = [int(x) for x in range(1, m+1)]
val = [int(0) for _ in range(n+m+1)]
for i in range(n):
    for j in range(m):
        tmp = arr_n[i]+arr_m[j]
        val[tmp] += 1
res = []
max_val = max(val)
for i in range(len(val)):
    if val[i] == max_val:
        res.append(i)
for x in res:
    print(x, end=' ')
'''

# 해설

n, m = map(int, input().split())
cnt = [0] * (n + m + 3)
max = -214700000
for i in range(1, n + 1):
    for j in range(1, m + 1):
        cnt[i + j] += 1
for i in range(n+m+1):
    if cnt[i] > max:
        max = cnt[i]
for i in range(n+m+1):
    if cnt[i] == max:
        print(i, end=' ')
