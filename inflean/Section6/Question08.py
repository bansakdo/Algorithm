import sys

sys.stdin = open("input.txt", "rt")

# 8번 문제. 순열 구하기

# 내 풀이
'''
def DFS(L):
    global cnt
    if L == m:
        for x in ch:
            print(x, end=' ')
        print()
        cnt += 1
        return
    else:
        for i in range(1, n + 1):
            if i not in ch:
                ch.append(i)
                DFS(L + 1)
                ch.pop()
            else:
                continue


if __name__ == "__main__":
    n, m = map(int, input().split())
    ch = []
    cnt = 0

    DFS(0)
    print(cnt)
'''

# 해설
'''
'''
def DFS(L):
    global cnt
    if L == m:
        for j in range(L):
            print(res[j], end=' ')
        print()
        cnt += 1
    else:
        for i in range(1, n + 1):
            if ch[i] == 0:
                ch[i] = 1
                res[L] = i
                DFS(L + 1)
                ch[i] = 0


if __name__ == "__main__":
    n, m = map(int, input().split())
    res = [0] * n
    ch = [0] * (n + 1)
    cnt = 0
    DFS(0)
    print(cnt)
