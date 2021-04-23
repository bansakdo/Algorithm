import sys

sys.stdin = open("input.txt", "rt")


# 5번 문제. 동전 분배하기


# 내 풀이
'''
def DFS(L, A, B, C):
    global minimum
    if L == n:
        if A != B and B != C and A != C:
            gap = max(A, B, C) - min(A, B, C)
            if gap < minimum:
                minimum = gap
    else:
        DFS(L + 1, A + coins[L], B, C)
        DFS(L + 1, A, B + coins[L], C)
        DFS(L + 1, A, B, C + coins[L])


if __name__ == "__main__":
    n = int(input())
    coins = [int(input()) for _ in range(n)]
    minimum = 2147000000

    DFS(0, 0, 0, 0)
    print(minimum)
'''



# 해설
'''
DFS 문제는 상태트리부터 만들면 된다.
사람은 세명이기때문에 한 노드에서 자식노드는 3개씩.
money라는 리스트에 사람들의 돈을 저장.
'''

def DFS(L):
    global res
    if L == n:                      # 상태트리 마지막까지 갔을 때, 마무리
        cha = max(money) - min(money)
        if cha < res:
            tmp = set()
            for x in money:
                tmp.add(x)
            if len(tmp) == 3:
                res = cha

    else:                           # 상태트리에서 가지를 뻗어나감. (자식노드들로 계속 이동)
        for i in range(3):          # 사람이 3명이기 때문에 3씩 반복.
            money[i] += coin[L]
            DFS(L + 1)
            money[i] -= coin[L]

if __name__ == "__main__":
    n = int(input())
    coin = []
    money = [0] * 3
    res = 2147000000
    for i in range(n):
        coin.append(int(input()))
    DFS(0)
    print(res)


