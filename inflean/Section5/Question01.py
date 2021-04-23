import sys
from collections import deque

sys.stdin = open("input.txt", "rt")

# 1번 문제. 가장 큰 수
'''
# 내 풀이
a, b = map(int, input().split())
a = str(a)
a = list(map(int, a))                                           # 숫자를 리스트로 만듦.
processed = 0                                                   # 마지막으로 처리한 숫자 위치

# b만큼 숫자를 없애서 b가 0이거나 리스트 마지막에 없애야 하는 개수가 남은 개수보다 크면 빠져나감.
while b > 0 and processed + b < len(a):
    print("a:\t\t\t", a)
    print("processed:\t", processed)
    print("b:\t\t\t", b)
    print("비교대상:\t\t", a[processed: processed + b + 1])

    largest = max(a[processed: processed + b + 1])              # 최대 b개를 지울 수 있으므로 b + 1개를 비교
    largest_idx = int(processed + a[processed: processed + b + 1].index(largest))      # largest의 index

    print("largest:\t", largest)
    print("largest_idx:", largest_idx, "\n")

    a = a[:processed] + a[largest_idx:]                         # processed와 largest 사이의 값들 지우기
    b -= largest_idx - processed
    processed += 1                                              # 숫자가 앞부터 1개씩 정해지므로 processed는 1씩 추가

if b > 0:
    for i in range(b):
        lowest = min(enumerate(a[processed:]), key=lambda x: x[1])
        idx = processed + lowest[0]
        a.pop(idx)

for x in a:
    print(x, end='')
'''

# 해설 풀이 들은 후
# '''
a, b = map(int, input().split())
a = str(a)
a = list(map(int, a))                                           # 숫자를 리스트로 만듦.
res = [a[0]]
for x in a[1:]:
    while True:
        if b < 0:
            res.append(x)
            break
        if len(res) > 0 and res[-1] < x :
            res.pop()
            b -= 1
        else:
            res.append(x)
            break

if b > 0:
    res = res[:-b]

for x in res:
    print(x, end='')
# '''


# 해설
# Stack은 Last In First Out. 나중에 들어간 것이 먼저 나옴.
# 파이썬에서는 리스트로 stack 구조를 활용할 수 있음.
# 각 숫자가 자기 앞에 있는 수가 자기보다 작으면 앞 숫자를 지우고 자신이 들어가는 방법.
'''
num, m = map(int, input().split())
num = list(map(int, str(num)))
stack = []

for x in num:
    while stack and m > 0 and stack[-1] < x:
        stack.pop()
        m -= 1
    stack.append(x)

if m != 0:
    stack = stack[:-m]
res = ''.join(map(str, stack))
print(res)
'''
