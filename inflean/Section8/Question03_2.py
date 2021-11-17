import sys

sys.stdin = open("input.txt", "rt")


# 도전과제. 돌다리 건너기(bottom-up)

n = int(input())
cnt = 0
dy = [0] * (n+1)
dy[1] = 2
dy[2] = 3

for i in range(3, n+1):
    dy[i] = dy[i - 1] + dy[i - 2]
print(dy[n])

