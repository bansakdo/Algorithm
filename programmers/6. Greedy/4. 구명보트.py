
# 내 풀이
# '''
def solution(people, limit):
    answer = 0

    people.sort(reverse=True)
    lt, rt = 0, len(people) - 1

    while lt <= rt:
        if limit >= people[lt] + people[rt]:
            rt -= 1
        lt += 1
        answer += 1

    return answer
# '''


people = [70, 50, 80, 50]
limit = 100

print(solution(people, limit))

