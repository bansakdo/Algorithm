import heapq

# 내 풀이
'''
def solution(jobs):
    size = len(jobs)
    now = 0
    prev = -1
    heap = []
    tot_time = []
    while len(tot_time) < size:

        for i in range(len(jobs)):
            if prev < jobs[i][0] <= now:
                heapq.heappush(heap, [jobs[i][1], jobs[i][0]])
        if len(heap) > 0:
            processing = heapq.heappop(heap)
            prev = now
            now += processing[0]
            tot_time.append(now - processing[1])
        else:
            now += 1
    answer = sum(tot_time) // size
    return answer
'''

# 다른사람 풀이
# '''
import heapq
from collections import deque

def solution(jobs):
    tasks = deque(sorted([(x[1], x[0]) for x in jobs], key=lambda x: (x[1], x[0])))
    q = []
    heapq.heappush(q, tasks.popleft())
    current_time, total_time = 0, 0
    while len(q) > 0:
        dur, arr = heapq.heappop(q)
        current_time = max(current_time + dur, arr + dur)
        total_time += current_time - arr
        while len(tasks) > 0 and tasks[0][1] <= current_time:
            heapq.heappush(q, tasks.popleft())
        if len(tasks) > 0 and len(q) == 0:
            heapq.heappush(q, tasks.popleft())
    return total_time // len(jobs)
# '''

# 다른사람 풀이. heap 사용 X. 제일 빠름.
'''
def solution(jobs):
    answer = 0
    start = 0  # 현재까지 진행된 작업 시간
    length = len(jobs)

    jobs = sorted(jobs, key=lambda x: x[1])  # 소요시간 우선 정렬

    while len(jobs) != 0:
        for i in range(len(jobs)):
            if jobs[i][0] <= start:
                start += jobs[i][1]
                answer += start - jobs[i][0]
                jobs.pop(i)
                break
            # 해당시점에 아직 작업이 들어오지 않았으면 시간 ++
            if i == len(jobs) - 1:
                start += 1

    return answer // length
'''


# jobs = [[0, 3], [1, 9], [2, 6]]     # => 9
# jobs = [[0, 3], [2, 3], [3, 5]]     # => 5
jobs = [[0, 3], [5, 3], [5, 2], [6, 2]]     # => 3.75


print(solution(jobs))
