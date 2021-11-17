import sys

sys.stdin = open("input.txt", "rt")

# 10번 문제. 역수열(그리디)
# '''
# 내 풀이
n = int(input())
a = list(map(int, input().split()))
res = [int(0) for _ in range(n)]            # 전체 0으로 초기화

for i in range(n):
    cnt = 0
    for j in range(n):
        if cnt >= a[i] and res[j] == 0:
            res[j] = i + 1
            break
        elif res[j] == 0:
            cnt += 1
    print(res)

for x in res:
    print(x, end=' ')
# '''

# 해설
'''
n = int(input())
a = list(map(int, input().split()))

seq = [0]*n

for i in range(n):
    for j in range(n):
        
        if a[i] == 0 and seq[j] == 0:
            seq[j] = i + 1
            break
        elif seq[j] == 0:
            a[i] -= 1

for x in seq:
    print(x, end=' ')
'''
