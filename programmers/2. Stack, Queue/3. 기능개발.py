# from collections import deque

# 내가 푼거
'''
def solution(progresses, speeds):
    answer = [1]
    size = len(progresses)
    _list = []

    for i in range(size):
        lead_time = (100 - progresses[i]) // speeds[i] + (0 if (100 - progresses[i]) % speeds[i] == 0 else 1)
        _list.append(lead_time)

    for i in range(1, size):
        if _list[i] <= _list[i-1]:
            _list[i] = _list[i-1]
            answer[-1] += 1
        else:
            answer.append(1)

    return answer
'''
'''
from collections import deque

def solution(progresses, speeds):
    answer = []
    queue = deque(enumerate(progresses))
    
    push = 0
    idx = 0
    while queue:
        now = queue.popleft()
        if now[1] + speeds[now[0]] >= 100 and now[0] == idx:
            idx += 1
            push += 1
            continue
        else:
            queue.append([now[0], now[1] + speeds[now[0]]])
        if push != 0:
            answer.append(push)
            push = 0
    
    answer.append(push)
            
    return answer
'''

# 다른사람이 푼거
# '''
def solution(progresses, speeds):
    Q=[]
    for p, s in zip(progresses, speeds):
        if len(Q)==0 or Q[-1][0]<-((p-100)//s):
            Q.append([-((p-100)//s),1])
        else:
            Q[-1][1]+=1
        print((p-100)//s)
    return [q[1] for q in Q]

# '''

# progresses = [93, 30, 55]
# speeds = [1, 30, 5]
# progresses = [95, 90, 99, 99, 80, 99]
# speeds = [1, 1, 1, 1, 1, 1]
progresses = [99, 90, 95, 0, 70, 71]
speeds = [1, 10, 3, 10, 1, 1]

print(solution(progresses, speeds))