import sys

sys.stdin = open("input.txt", "rt")

# 6번 문제. 가장 높은 탑 쌓기

# 내 풀이

n = int(input())
blocks = [[int(x) for x in input().split()] for _ in range(n)]
blocks.sort(reverse=True)
blocks.insert(0, [0, 0, 0])
res = [0] * (n+1)
res[0] = 0
height = 0


for i in range(1, n+1):
    top = 0
    for j in range(i-1, 0, -1):
        if blocks[i][0] < blocks[j][0] and blocks[i][2] < blocks[j][2] and top < res[j]:
            top = res[j]
    res[i] = top + blocks[i][1]
    if height < res[i]:
        height = res[i]
print(height)








