import sys

sys.stdin = open("input.txt", "rt")

# 3번 문제. 카드 역배치(정올 기출)

# 내가 푼거
'''
_list = [int(x) for x in range(21)]
for _ in range(10):
    start, end = map(int, input().split())
    sub_list = _list[end: start - 1: -1]
    _list[start: end + 1] = sub_list
_list.pop(0)
for x in _list:
    print(x, end=' ')
'''

# 해설
a = list(range(21))
for _ in range(10):
    s, e = map(int, input().split())
    for i in range((e-s+1)//2):
        a[s+i], a[e-i] = a[e-i], a[s+i]          # 두 변수 값 교환하는 방법(스왑)
a.pop(0)
for x in a:
    print(x, end=' ')

