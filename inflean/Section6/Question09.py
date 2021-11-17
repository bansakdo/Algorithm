import sys

sys.stdin = open("input.txt", "rt")

# 9번 문제. 수열 추측하기

# 내 풀이
'''
def DFS(L):
    if L == n - 1:
        if len(a[L]) == 1 and a[L][0] == m:
            print(a[0])
    else:
        tmp = []
        for i in range(n - L - 1):
            tmp.append(a[L][i] + a[L][i+1])
            DFS(L+1)


if __name__ == "__main__":
    n, m = map(int, input().split())
    a = []
    a.append([x for x in range(1, n+1)])
    print(a)
    DFS(0)
'''


# 해설

def DFS(L, sum):
    if L == n and sum == f:
        for x in p:
            print(x, end=' ')
        sys.exit(0)
    else:
        for i in range(1, n+1):
            if ch[i] == 0:
                ch[i] = 1
                p[L] = i
                DFS(L + 1, sum + (p[L] * b[L]))
                ch[i] = 0


if __name__ == "__main__":
    n, f = map(int, input().split())
    p = [0] * n
    b = [1] * n
    ch = [0] * (n + 1)

    for i in range(1, n):
        b[i] = (b[i - 1] * (n - i)) // i         # 조합
    DFS(0, 0)





