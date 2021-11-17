
'''
7 5
100
400
300
100
500
101
400

=> 500


8 6
100
400
300
101
600
101
400
200

=> 600




'''



n, m = map(int, input().split())
daily = list(int(input()) for _ in range(n))
lt = min(daily)
rt = sum(daily)

while lt <= rt:
    mid = (lt + rt) // 2
    charge = mid
    num = 1
    for i in range(n):
        if charge < daily[i]:
            charge = mid
            num += 1
        charge -= daily[i]

    if num > m or mid < max(daily):
        lt = mid + 1
    else:
        rt = mid - 1
        k = mid

print(k)



