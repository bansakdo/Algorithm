import sys

sys.stdin = open("input.txt", "rt")

# 6번 문제. 씨름선수(그리디)

# 내 풀이
'''
n = int(input())
people = [[int(x) for x in input().split()] for _ in range(n)]
fail = []                       # 탈락자 리스트
for i in range(n):
    if fail.__contains__(i):    # i번째 사람이 이미 탈락자이면 다음사람으로 넘어감
        continue
    n_height = people[i][0]     # 현재 선택된 i번째 사람의 키
    n_weight = people[i][1]     # 현재 선택된 i번째 사람의 몸무게
    for j in range(n):          # 현재 선택된 i번째 사람과 비교할 대조군
        if fail.__contains__(j) or i == j:          # j번째 사람이 이미 탈락자이거나 i번째 사람과 동일인이면 다음 사람으로 넘어감
            continue
        t_height = people[j][0]                                 # j번째 사람의 키
        t_weight = people[j][1]                                 # j번째 사람의 몸무게
        if n_height < t_height and n_weight < t_weight:         # i번째 사람이 j번째 사람보다 키, 몸무게 모두 작을 때.
            fail.append(i)                                      # i번째 사람을 탈락자 리스트에 추가
            break                                               # i번째 사람은 더 비교할 필요 없으므로 다음사람으로 넘어감.
        elif n_height > t_height and n_weight > t_weight:       # i번째 사람이 j번째 사람보다 키, 몸무게 모두 클 때.
            fail.append(j)                                      # j번째 사람을 탈락자 리스트에 추가
print(n - len(fail))             # 전체 지원자 수에서 탈락자 수만큼 뺀 것이 합격자. 출력.
'''


# 해설
# 키를 내림차순 정렬 한 후에, 몸무게만 비교해가면 관찰.
# 기존 largest 보다 큰 몸무게가 있으면 카운트.
n = int(input())
body = []
for i in range(n):                      # 입력
    a, b = map(int, input().split())
    body.append((a, b))                 # 키, 몸무게
body.sort(reverse=True)                 # 내림차순 정렬
tot = 0
cnt = 0
for x, y in body:
    if y > tot:
        tot = y
        cnt += 1
print(cnt)


