import sys

sys.stdin = open("input.txt", "rt")

# 8번 문제. 곶감(모래시계)

# 내가 푼거
'''
n = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(n)]
m = int(input())

#  회전
for _ in range(m):
    c = list(map(int, input().split()))
    row = c[0] - 1
    direction = c[1]
    if direction == 0:
        num = c[2] % n
    else:
        num = n - c[2] % n
    tmp = matrix[row][num:n]
    tmp += matrix[row][:num]
    matrix[row] = tmp

# 모래시계 합
tot = 0
for i in range(n // 2 + 1):
    for j in range(i, n - i):
        tot += matrix[i][j]
        if n - i - 1 != n // 2:
            tot += matrix[n - i - 1][j]

print(tot)
'''

# 해설
n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
m = int(input())
for i in range(m):
    h, t, k = map(int, input().split())
    if t == 0:
        for _ in range(k):
            a[h-1].append(a[h-1].pop(0))
    else:
        for _ in range(k):
            a[h-1].insert(0, a[h-1].pop())
res = 0
s = 0
e = n - 1
for i in range(n):
    for j in range(s, e+1):
        res += a[i][j]
    if i < n // 2:
        s += 1
        e -= 1
    else:
        s -= 1
        e += 1
print(res)

