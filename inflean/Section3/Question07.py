import sys

sys.stdin = open("input.txt", "rt")

# 7번 문제. 사과나무(다이아몬드)

'''
n = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(n)]

center_index = n // 2
apples = 0
for i in range(center_index + 1):
    for j in range(center_index - i, center_index + i + 1):
        apples += matrix[i][j]
        if i != center_index:
            apples += matrix[n-1-i][j]
print(apples)
'''


# 해설

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
res = 0
s = e = 0
for i in range(n):
    for j in range(s, e + 1):
        res += a[i][j]
    if i < n // 2:
        s -= 1
        e += 1
    else:
        s += 1
        e -= 1
print(res)





