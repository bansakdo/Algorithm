import sys
import itertools as it              # 순열 라이브러리

# 12번 문제. 라이브러리를 이용한 순열 (순열 추측하기)
sys.stdin = open("input.txt", "rt")
n, f = map(int, input().split())
b = [1] * n
for i in range(1, n):
    b[i] = b[i - 1] * (n - i) / i
a = list(range(1, n + 1))

# for tmp in it.permutations(a):          # a 리스트 안의 데이터로 순열을 구해줌.
# for tmp in it.permutations(a, 3):       # a 리스트 안의 데이터로 사이즈가 3인 순열을 구해줌.

for tmp in it.permutations(a):
    sum = 0
    for L, x in enumerate(tmp):
        sum += (x * b[L])
    if sum == f:
        for x in tmp:
            print(x, end=' ')
        break


