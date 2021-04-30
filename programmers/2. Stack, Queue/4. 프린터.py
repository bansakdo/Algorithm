from collections import deque

# 내 풀이
'''
def solution(priorities, location):
    answer = 0
    priorities = deque(priorities)

    while priorities:
        if priorities[0] == max(priorities):
            priorities.popleft()
            answer += 1
            if location == 0:
                break
            location -= 1
        else:
            priorities.append(priorities.popleft())
            if location == 0:
                location = len(priorities) - 1
            else:
                location -= 1

    return answer
'''

def solution(priorities, location):
    queue = deque((i, p) for i, p in enumerate(priorities))
    answer = 0

    while True:
        cur = queue.popleft()
        if any(cur[1] < q[1] for q in queue):
            queue.append(cur)
        else:
            answer += 1
            if cur[0] == location:
                break
    return answer





# priorities = [2, 1, 3, 2]
# location = 2
priorities = [1, 1, 9, 1, 1, 1]
location = 0

print(solution(priorities, location))