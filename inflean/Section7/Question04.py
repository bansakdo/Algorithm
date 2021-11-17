import sys
import time

sys.stdin = open("input.txt", "rt")
start = time.time()


# 4번 문제. 동전 바꿔주기(DFS)
'''
def DFS(L, sum):
    global cnt
    if L == k:
        if sum == T:
            cnt += 1
        return
    else:
        # DFS(L + 1, sum)
        # for i in range(n[L] + 1):
        #     if sum + p[L] * i <= T:
        #         DFS(L + 1, sum + p[L] * i)
        for i in range(n[L] + 1):
            DFS(L + 1, sum + p[L] * i)


if __name__ == "__main__":
    T = int(input())
    k = int(input())
    p = []
    n = []
    for _ in range(k):
        a, b = map(int, input().split())
        p.append(a)
        n.append(b)
    cnt = 0

    DFS(0, 0)
    print(cnt)


    print("time :", time.time() - start)
'''

# 해설
'''
상태트리를 사용해 풀이
DFS에서 동전을 사용하는 경우부터 모두 사용하는 경우까지 모두 확인.
'''
# '''
def DFS(L, sum):
    global cnt
    if sum > T:
        return 
    if L == k:
        if sum == T:
            cnt += 1
    else:
        for i in range(cn[L] + 1):
            DFS(L + 1, sum + (cv[L] * i))

if __name__ == "__main__":
    T = int(input())
    k = int(input())
    cv = list()
    cn = list()
    for i in range(k):
        a, b = map(int, input().split())
        cv.append(a)
        cn.append(b)
    cnt = 0
    DFS(0, 0)
    print(cnt)

    print("time :", time.time() - start)
# '''