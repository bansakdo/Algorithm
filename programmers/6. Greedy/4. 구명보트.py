
# 내 풀이
# '''
def solution(people, limit):
    answer = 0

    people.sort(reverse=True)
    lt, rt = 0, len(people) - 1

    for i, first in enumerate(people):
        surplus = limit - first
        lt = i + 1
        if surplus >= people[rt]:
            rt -= 1
        answer += 1
        if lt > rt:
            break

    return answer
# '''

# 다른사람 풀이
'''
def solution(people, limit) :
    answer = 0
    people.sort()

    a = 0
    b = len(people) - 1
    while a < b :
        if people[b] + people[a] <= limit :
            a += 1
            answer += 1
        b -= 1
    return len(people) - answer
'''

people = [70, 50, 80, 50]
limit = 100

print(solution(people, limit))

