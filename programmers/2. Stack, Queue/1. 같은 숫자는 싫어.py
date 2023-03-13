



def solution(arr):
    answer = []

    for v in arr:
        if not answer or answer[-1] != v:
            answer.append(v)


    return answer



arr = [1, 1, 3, 3, 0, 1, 1]
print(solution(arr))