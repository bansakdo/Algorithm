import sys

sys.stdin = open("input.txt", "rt")

# 5번 문제. 수들의 합

# 내가 푼거
'''
n, m = map(int, input().split())
_list = [int(x) for x in input().split()]

cnt = 0

for i in range(n):
    sum = 0
    for j in range(i, n):
        sum += _list[j]
        if sum > m:
            break
        elif sum == m:
            cnt += 1
            break
print(cnt)
'''

# 해설
n, m = map(int, input().split())
a = list(map(int, input().split()))
lt = 0
rt = 1
tot = a[0]
cnt = 0
while True:
    if tot < m:
        if rt < n:
            tot += a[rt]
            rt += 1
        else:
            break
    elif tot == m:
        cnt += 1
        tot -= a[lt]
        lt += 1
    else:
        tot -= a[lt]
        lt += 1
print(cnt)



