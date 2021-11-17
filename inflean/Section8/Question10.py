import sys

sys.stdin = open("input.txt", "rt")


# 10번 문제. 동전교환


# 내 풀이

# 틀림
'''
n = int(input())
coin = list(map(int, input().split()))
m = int(input())

coin.sort(reverse=True)
cnt = 0

for i in range(n):
    cnt += m // coin[i]
    m %= coin[i]

print(cnt)
'''

# 4, 5 시간초과
'''
def DFS(L, remain):
    global cnt
    if L >= n:
        if remain == 0:
            s = sum(use)
            cnt = min(cnt, s)
            # print(use, s)
            return
    else:
        # print(L, remain, cnt)
        c = 0
        while remain >= 0:
            DFS(L+1, remain)
            use[L] += 1
            c += 1
            remain -= coin[L]
        remain += coin[L] * c
        use[L] -= c


if __name__ == "__main__":
    n = int(input())
    coin = list(map(int, input().split()))
    m = int(input())
    cnt = 2147000000
    use = [0] * n

    DFS(0, m)
    print(cnt)
'''

# 성공
'''
def DFS(L, remain, tot):
    global cnt
    if L >= n:
        if remain == 0:
            cnt = min(cnt, tot)
            return
    else:
        c = 0
        while remain >= 0 and tot <= cnt:
            DFS(L+1, remain, tot)
            c += 1
            tot += 1
            remain -= coin[L]
        tot -= c


if __name__ == "__main__":
    n = int(input())
    coin = list(map(int, input().split()))
    m = int(input())
    cnt = 2147000000

    DFS(0, m, 0)
    print(cnt)
'''

'''
# 해설 들은 후 냅색 알고리즘으로 풀이.
n = int(input())
coin = list(map(int, input().split()))
m = int(input())
dy = [m] * (m+1)
dy[0] = 0

for i in range(n):
    c = coin[i]
    for j in range(c, m+1):
        dy[j] = min(dy[j], dy[j-c] + 1)

print(dy[m])
'''


# 해설
'''
dy를 사용하여 풀이. dy는 [0] * (m+1) 으로 초기화. m원이 거슬러 주어야 할 돈이기 때문.
dy[j]에서 j를 거슬러 주는데 사용되는 최소 개수

'''

if __name__ == "__main__":
    n = int(input())
    coin = list(map(int, input().split()))
    m = int(input())
    dy = [1000] * (m + 1)
    dy[0] = 0

    for i in range(n):
        for j in range(coin[i], m+1):
            dy[j] = min(dy[j], dy[j-coin[i]] + 1)

    print(dy[m])



