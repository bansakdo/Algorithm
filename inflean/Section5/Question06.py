import sys
from collections import deque

sys.stdin = open("input.txt", "rt")


# 6번 문제. 응급실

# 내 풀이
'''
n, m = map(int, input().split())
risk = list(map(int, input().split()))
cnt = 0
risk = deque(risk)

while cnt < n:
    risk_max = max(risk)            # 가장 큰 위험도
    if risk[0] < risk_max:          # 위험도가 더 큰 환자가 존재할 경우
        tmp = risk.popleft()        # 현재 환자 뒤로 넘김
        risk.append(tmp)
        if m == 0:                  # 현재 환자가 목표이면 m값 변경
            m = len(risk) - 1
        else:
            m -= 1                  # 현재 환자가 목표가 아니라면 m을 -1 해줌
    else:                           # 현재 환자가 위험도 가장 큰 환자
        risk.popleft()              # 진료함
        cnt += 1                    # 진료 받은 사람 업데이트
        if m == 0:
            break
        else:
            m -= 1
print(cnt)
'''

# 해설
n, m = map(int, input().split())
Q = [(pos, val) for pos, val in enumerate(map(int, input().split()))]       # pos : 인덱스, val : 위험도. Q는 튜플
Q = deque(Q)
cnt = 0
while True:
    cur = Q.popleft()
    if any(cur[1] < x[1] for x in Q):           # Q의 모든 원소에 접근하여 위험도를 비교. any는 조건이 하나라도 참이면 참.
        Q.append(cur)
    else:
        cnt += 1
        if cur[0] == m:
            break
print(cnt)






