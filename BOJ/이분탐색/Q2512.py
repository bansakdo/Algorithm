'''
INPUT
4
120 110 140 150
485
=> 127

5
120 110 190 180 300
600
=> 123

5
120 110 230 300 190
900
=> 250

'''


# 2512번. 예산

n = int(input())
r = list(map(int, input().split()))
total = int(input())
a = 0
b = max(r)

while a <= b:
    mid = (a + b) // 2
    tmp = 0

    for i in range(n):
        if r[i] <= mid:
            tmp += r[i]
        else:
            tmp += mid

    if tmp > total:
        b = mid - 1
    else:
        a = mid + 1

print(b)

