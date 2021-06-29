


N, C = map(int, input().split())
houses = list(int(input()) for _ in range(N))
houses.sort()

lt = 1
rt = houses[-1] - houses[0]
rst = rt

while lt <= rt:
    mid = (rt + lt) // 2


    cnt = 1
    start = houses[0]
    for i in range(1, N):
        distance = houses[i] - start
        if mid <= distance:
            cnt += 1
            start = houses[i]

    if cnt < C:
        rt = mid - 1
    else:
        rst = mid
        lt = mid + 1

print(rst)








'''
6 4
1
2
3
9
11
12
=> 2
1 12 6
1 5 3
1 2 1
2 2 2


5 3
1
2
8
4
9
=> 3
[1, 2, 4, 8, 9]



'''