
N, K, D = map(int, input().split())
rules = [list(map(int, input().split())) for _ in range(K)]
rst = -1

lt = 0
rt = N

while lt <= rt:
    mid = (lt + rt) // 2

    i = 0
    cnt = 0
    for rule in rules:
        A, B, C = rule
        end = min(B, mid)
        if end >= A:
            cnt += (end - A) // C + 1

    if cnt >= D:
        rst = mid
        rt = mid - 1
    else:
        lt = mid + 1

print(rst)


