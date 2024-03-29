import sys

sys.stdin = open("input.txt", "rt")


# 6번 문제. 자릿수의 합.

# 내가 푼거
'''
def digit_sum(x):
    res = 0
    while x / 10 > 0:
        res += (x % 10)
        x = x // 10
    return res


n = int(input())
arr = [int(x) for x in input().split()]
val = [digit_sum(x) for x in arr]
max_num = 0
idx = 0
for i in range(n):
    if max_num < val[i]:
        max_num = val[i]
        idx = i
print(arr[idx])
'''

# 해설
n = int(input())
a = list(map(int, input().split()))

# 방법 1
def digit_sum(x):
    sum = 0
    while x > 0:
        sum += x % 10
        x = x // 10
    return sum
# 방법 2
def digit_sum_2(x):
    sum = 0
    for i in str(x):
        sum += int(i)
    return sum


max = -2147000000
for x in a:
    tot = digit_sum(x)
    if tot > max:
        max=tot
        res = x
print(res)



