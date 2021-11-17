import sys

sys.stdin = open("input.txt", "rt")

# 10번 문제. 조합 구하기

# 내 풀이
'''
def DFS(L):
    global res, cnt
    if L == m:
        for x in res:
            print(x, end=' ')
        cnt += 1
        print()
        return
    else:
        tmp = 1 + (res[-1] if len(res) != 0 else 0)
        for i in range(tmp, n + 1):
            res.append(i)
            DFS(L + 1)
            res.pop()


if __name__ == "__main__":
    n, m = map(int, input().split())
    cnt = 0
    ch = [0] * (n+1)
    res = []

    DFS(0)
    print(cnt)
'''


# 해설
def DFS(L, s):
    global cnt
    if L == m:
        for j in range(L):
            print(res[j], end=' ')
        cnt += 1
        print()
    else:
        for i in range(s, n + 1):
            res[L] = i
            DFS(L + 1, i + 1)

if __name__ == "__main__":
    n, m = map(int, input().split())
    res = [0] * (n + 1)
    cnt = 0
    DFS(0, 1)
    print(cnt)
