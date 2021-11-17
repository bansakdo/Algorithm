from collections import deque

if __name__ == "__main__":
    N, K = map(int, input().split())
    name_len = [len(input()) for _ in range(N)]
    cnt = 0
    __list = [deque() for _ in range(21)]

    for i, v in enumerate(name_len):
        while __list[v] and i - __list[v][0] > K:
            __list[v].popleft()
        if __list[v]:
            cnt += len(__list[v])
        __list[v].append(i)

    print(cnt)





