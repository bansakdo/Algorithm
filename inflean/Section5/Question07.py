import sys
from collections import deque

sys.stdin = open("input.txt", "rt")

# 7번 문제. 교육과정 설계

# 내 풀이
'''
essential = [x for x in input()]
n = int(input())
subjects = [input() for _ in range(n)]

for i in range(n):
    tmp = []
    for x in subjects[i]:
        if essential.__contains__(x) and not tmp.__contains__(x):
            tmp.append(x)
    else:
        if tmp == essential:
            print("#%d YES" % (i + 1))
        else:
            print("#%d NO" % (i + 1))
'''

# 해설
need = input()
n = int(input())
for i in range(n):
    plan = input()                      # 짠 수업표
    dq = deque(need)                    # deque화
    for x in plan:
        if x in dq:                     # x가 dq 안에 있다면
            if x != dq.popleft():       # dq에서 popleft 한 값이 x와 다르면
                print("#%d NO" % (i + 1))
                break
    else:
        if len(dq) == 0:                # dq에 남은 원소가 있다면 YES, 아니면 NO
            print("#%d YES" & (i + 1))
        else:
            print("#%d NO" & (i + 1))


