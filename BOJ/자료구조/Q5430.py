import sys
from collections import deque
from collections import Counter

for _ in range(int(sys.stdin.readline())):
    try:
        p = sys.stdin.readline()
        n = int(sys.stdin.readline())
        arr = sys.stdin.readline()[1:-2]
        if len(arr) > 0:
            arr = deque(map(int, arr.split(',')))
        else:
            arr = deque(arr)

        isAsc = True

        if 'D' in p:
            num_p = Counter(p).get('D')
            if num_p > n:
                raise ValueError
            elif num_p == n:
                print("[]")
                continue

        for cmd in p:
            if cmd == 'R':
                isAsc = not isAsc
            if cmd == 'D':
                if len(arr) <= 0:
                    raise ValueError
                if isAsc:
                    arr.popleft()
                else:
                    arr.pop()
        else:
            if not isAsc:
                arr.reverse()
            print(str(list(arr)).replace(' ', ''))
    except:
        print("error")
