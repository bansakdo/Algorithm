import sys


def dfs(num):
    global P, Q, arr
    if num < 1:
        return 1
    elif num in arr:
        return arr[num]
    arr[num] = dfs(num//P) + dfs(num//Q)
    return arr[num]


if __name__ == "__main__":
    N, P, Q = map(int, sys.stdin.readline().split())
    cnt = 0
    arr = {}


    print(dfs(N))
