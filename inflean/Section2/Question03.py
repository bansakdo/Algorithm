import sys

sys.stdin = open("input.txt", "rt")

# 3번 문제. K번째 큰 수

# 내가 푼거
'''
N, K = map(int, input().split())
cards = list(map(int, input().split()))
values = []

for i in range(N - 2):
    first = cards[i]
    for j in range(i + 1, N - 1):
        second = cards[j]
        for k in range(j + 1, N):
            third = cards[k]
            total = first + second + third
            values.append(total)

values.sort(reverse=True)
index = 0
while index + 1 < len(values) - 1:
    if values[index] == values[index + 1]:
        values.pop(index + 1)
        continue
    index += 1
print(values[K - 1])
'''

# 해설
n, k = map(int, input().split())
a = list(map(int, input().split()))
res = set()                     # set은 중복 허용 X
for i in range(n):
    for j in range(i+1, n):
        for m in range(j+1, n):
            res.add(a[i]+a[j]+a[m])
res = list(res)
res.sort(reverse=True)
print(res[k-1])
