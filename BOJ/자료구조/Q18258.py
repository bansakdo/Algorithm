from collections import deque


N = int(input())
commands = [input() for _ in range(N)]

queue = deque()

for cmd in commands:
    if cmd[:4] == 'push':
        queue.append(int(cmd[5:]))
    elif cmd == 'size':
        print(len(queue))
    elif cmd == 'empty':
        if queue:
            print(0)
        else:
            print(1)
    else:
        if not queue:
            print(-1)
        elif cmd == 'pop':
            print(queue.popleft())
        elif cmd == 'front':
            print(queue[0])
        elif cmd == 'back':
            print(queue[-1])


