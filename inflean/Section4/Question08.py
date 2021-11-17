import sys
from collections import deque

sys.stdin = open("input.txt", "rt")

# 8번 문제. 침몰하는 타이타닉(그리디)

# 내 풀이
n, m = map(int,input().split())
weight = list(map(int, input().split()))
weight.sort(reverse=True)                               # 주어진 무게 제한을 최대한 채우기 위해서
cnt = 0
i = 0
while len(weight) > 0:
    available = m - weight[0]
    for x in weight[1:]:
        if x <= available:
            cnt += 1
            weight.pop(0)
            weight.remove(x)
            break
    else:
        cnt += 1
        weight.pop(0)

print(cnt)


# 해설
'''
오름차순 정렬 후
왼쪽 끝(가벼운 사람)과 오른쪽 끝(무거운 사람)을 순차적으로 비교
왼쪽이 기준이 되며, 두 사람의 합이 무게제한을 넘으면 무거운 사람은 혼자 배를 타야 하므로 그 앞사람으로 넘어간다.
'''
'''
n, limit = map(int, input().split())
p = list(map(int, input().split()))
p.sort()

cnt = 0
while p:
    if len(p) == 1:             # p가 한 개 남았을 때 뒤에서 오류 발생.
        cnt += 1
        break
    if p[0] + p[-1] > limit:
        p.pop()
        cnt += 1
    else:
        p.pop(0)
        p.pop()
        cnt += 1
print(cnt)
'''
'''
list는 앞에서 pop 하게 되면 모든 자료가 앞쪽으로 옮겨지는 작업 실행.
따라서 일이 많아짐.
deque는 앞쪽 자료가 없어지면 자료를 앞당기는 것이 아닌 시작하는 요소를 가리키는 포인터 주소를 바꿈.
'''

n, limit = map(int, input().split())
p = list(map(int, input().split()))
p.sort()
p = deque(p)

cnt = 0
while p:
    if len(p) == 1:             # p가 한 개 남았을 때 뒤에서 오류 발생.
        cnt += 1
        break
    if p[0] + p[-1] > limit:
        p.pop()
        cnt += 1
    else:
        p.popleft()             # 리스트에서 p.pop(0)과 같은 역할.
        p.pop()
        cnt += 1
print(cnt)

