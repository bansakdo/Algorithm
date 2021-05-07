from collections import deque

'''
def solution(people, limit):
    answer = 0
    people.sort()

    while people:
        first = people.pop()
        surplus = limit - first
        second = -1
        for idx, p in enumerate(people):
            if p <= surplus:
                second = idx
        if second != -1:
            people.pop(second)
        answer += 1
    return answer
'''


'''
def solution(people, limit):
    answer = 0

    people.sort()
    ch = [0] * len(people)

    # while any(c == 0 for c in ch):
    for i, first in enumerate(people):
        if ch[i] == 1:
            continue
        surplus = limit - first
        ch[i] = 1
        for idx in range(len(people) - 1, -1, -1):
            if ch[idx] == 0 and people[idx] <= surplus:
                ch[idx] = 1
                break
        answer += 1

    return answer
'''

def solution(people, limit):
    answer = 0

    people.sort(reverse=True)
    ch = [0] * len(people)

    # while any(c == 0 for c in ch):
    for i, first in enumerate(people):
        if ch[i] == 1:
            continue
        surplus = limit - first
        ch[i] = 1
        # second = -1
        for idx in range(len(people) - 1, -1, -1):
            if ch[idx] == 0 and people[idx] <= surplus:
                # second = idx
                ch[idx] = 1
                break
        # if second != -1:
        #     people[second]
        answer += 1


    return answer

people = [70, 50, 80, 50]
limit = 100

print(solution(people, limit))

