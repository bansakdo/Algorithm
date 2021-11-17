import sys

sys.stdin = open("input.txt", "rt")


# 6번 문제. 중복순열 구하기

# 내 풀이
'''
def DFS(L):
    global cnt
    if L == m:
        cnt += 1
        for x in res:
            print(x, end=' ')
        print()
        return
    else:

        for i in range(1, n+1):
            res.append(i)
            DFS(L+1)
            res.pop()

if __name__ == "__main__":
    n, m = map(int, input().split())
    cnt = 0
    res = []

    DFS(0)
    print(cnt)
'''


# 해설
'''
DFS에서 한개의 부모노드에서 n개의 자식노드 생성. Level은 m까지.
'''

def DFS(L):
    global cnt
    if L == m:
        for j in range(m):
            print(res[j], end=' ')
        print()
        cnt = cnt + 1
    else:
        for i in range(1, n + 1):
            res[L] = i
            DFS(L+1)


if __name__ == "__main__":
    n, m = map(int, input().split())
    res = [0] * n
    cnt = 0
    DFS(0)
    print(cnt)
