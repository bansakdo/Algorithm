import time

start = time.time()

# 내 풀이
'''
def solution(n, lost, reserve):
    answer = n - len(lost)

    complete = []
    for l in lost:
        if l in reserve:
            answer += 1
            reserve.remove(l)
            complete.append(l)
    else:
        for c in complete:
            lost.remove(c)


    for l in lost:
        if l-1 in reserve:
            answer += 1
            reserve.remove(l-1)
        elif l+1 in reserve:
            answer += 1
            reserve.remove(l+1)
        if not reserve:
            break

    return answer
'''

# 다른사람 풀이 1
'''
def solution(n, lost, reserve):
    # _reserve = [r for r in reserve if r not in lost]
    # _lost = [l for l in lost if l not in reserve]
    _reserve = list(set(reserve) - set(lost))
    _lost = list(set(lost) - set(reserve))
    for r in _reserve:
        f = r - 1
        b = r + 1
        if f in _lost:
            _lost.remove(f)
        elif b in _lost:
            _lost.remove(b)
    return n - len(_lost)
'''

# 다른사람 풀이 2
'''
def solution(n, lost, reserve):

    reserve = set(reserve)

    for size in [0, 1, -2]:
        lost = set(map(lambda x : x+size, lost))
        # print(lost)
        reserve, lost = reserve - lost, lost - reserve

    # print(lost)
    return n - len(lost)
'''

'''

n = 5
lost = [2, 4]
reserve = [1, 3, 5]
=> 5

n = 5
lost = [2, 4]
reserve = [3]
=> 4

n = 3
lost = [3]
reserve = [1]
=> 2

n = 10
lost = [3, 4, 7, 9]
reserve = [1, 2, 4, 8]
=> 9

lost = [3, 4, 6, 7, 8, 9]
reserve = [1, 3, 4, 5, 7, 8]
=> 9
'''

n = 30
lost = [3, 4, 6, 7, 8, 9, 11, 13, 17, 21, 22, 23, 29, 30]
reserve = [1, 3, 4, 5, 7, 8, 10, 12, 13, 16, 19, 20, 21, 23, 24, 28]

print(solution(n, lost, reserve))

print(time.time() - start)