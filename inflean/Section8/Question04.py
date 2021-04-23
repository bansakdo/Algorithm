import sys

sys.stdin = open("input.txt", "rt")


# 4번 문제. 최대 부분 증가수열 (LIS)
'''
def DFS(L, s):
    global length
    if s == n:
        length = max(length, L)
    elif s < n:
        for i in range(s, n):
            if arr[i] > res[-1]:
                res.append(arr[i])
                DFS(L + 1, i + 1)
                res.pop()
            DFS(L, i + 1)

if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    length = 0
    res = [0]

    DFS(0, 0)
    print(length)
'''


# 해설

n = int(input())
arr = list(map(int, input().split()))
arr.insert(0, 0)
dy = [0] * (n + 1)
dy[1] = 1
res = 0

for i in range(2, n + 1):
    max = 0
    for j in range(i-1, 0, -1):
        if arr[j] < arr[i] and dy[j] > max:
            max = dy[j]
    dy[i] = max + 1
    if dy[i] > res:
        res = dy[i]






