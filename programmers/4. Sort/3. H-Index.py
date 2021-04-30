
# 내 풀이
'''
def solution(citations):
    answer = len(citations)
    citations.sort(reverse=True)

    for i, v in enumerate(citations):
        if v < i+1:
            answer = i
            break

    return answer
'''


# 다른사람 풀이
def solution(citations):
    citations.sort(reverse=True)
    answer = max(map(min, enumerate(citations, start=1)))


    print(list(enumerate(citations, start=1)))
    print(list(map(min, enumerate(citations, start=1))))

    return answer


# citations = [3, 0, 6, 1, 5]
# citations = [3, 0, 6, 1, 5, 6, 1]
citations = [3, 0, 6, 1, 5, 5, 1, 5]
# citations = [9, 9, 9, 9, 9, 9, 9, 9]
print(solution(citations))