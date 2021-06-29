from collections import deque

test_case = int(input())
for _ in range(test_case):
    n, m = map(int, input().split())
    _list = deque(map(int, input().split()))

    priority = max(_list)

    while True:
        now = _list.popleft()
        m -= 1
        if now != priority:
            _list.append(now)
            if m == -1:
                m = len(_list) - 1
            continue
        else:
            if len(_list) != 0:
                priority = max(_list)
            if m == -1:
                print(n - len(_list))
                break










