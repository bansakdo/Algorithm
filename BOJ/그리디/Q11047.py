

N, K = map(int, input().split())
coins = list(int(input()) for _ in range(N))
cnt = 0

for i in range(N-1, -1, -1):
    used_coin = K // coins[i]
    cnt += used_coin
    K -= coins[i] * used_coin

print(cnt)

'''
4 84
1
7
10
50

50      1
10      3
1       4
8

50      1
10      2
7       2
5

'''