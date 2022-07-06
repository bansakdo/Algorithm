from collections import deque

N, M = map(int, input().split())
point = list(map(int, input().split()))
plus = []
minus = []
for p in point:
    if p < 0:
        minus.append(p)
    else:
        plus.append(p)
plus.sort()
minus = deque(sorted(minus))
far = max(abs(x) for x in point)


dist = 0
while minus:
    turn_point = abs(minus.popleft())
    dist += turn_point * 2
    if turn_point == far:
        dist -= turn_point
    for _ in range(M - 1):
        if minus:
            minus.popleft()
while plus:
    turn_point = plus.pop()
    dist += turn_point * 2
    if turn_point == far:
        dist -= turn_point
    for _ in range(M - 1):
        if plus:
            plus.pop()

print(dist)

