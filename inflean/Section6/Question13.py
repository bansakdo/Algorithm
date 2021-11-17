import sys
import itertools as it

# 13번. 라이브러리를 이용한 조합
sys.stdin = open("input.txt", "rt")
n, k = map(int, input().split())
a = list(map(int, input().split()))
m = int(input())

cnt = 0
for x in it.combinations(a, k):         # 조합. a개에서 k개 추출
    if sum(x) % m == 0:
        cnt += 1
print(cnt)

