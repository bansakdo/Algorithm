




def solution(answers):
    answer = []
    a1 = [1, 2, 3, 4, 5]
    a2 = [2, 1, 2, 3, 2, 4, 2, 5]
    a3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    submit = [a1, a2, a3]
    length = [len(a1), len(a2), len(a3)]
    size = len(answers)
    cnt = [0, 0, 0]

    for i in range(size):
        for j in range(3):
            if submit[j][i % length[j]] == answers[i]:
                cnt[j] += 1

    highest = max(cnt)
    for idx, x in enumerate(cnt):
        if highest == x:
            answer.append(idx + 1)

    return answer


print(solution([1, 2, 3, 4, 5]))
print(solution([1, 3, 2, 4, 2]))
print(solution([2, 1, 2, 3, 5]))

