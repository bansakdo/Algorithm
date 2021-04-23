


def solution(name):
    alphabet_number = [min(ord(i) - ord("A"), ord("Z") - ord(i)+1) for i in name]
    idx, answer = 0, 0
    while True:
        answer += alphabet_number[idx]
        alphabet_number[idx] = 0
        if not any(alphabet_number):
            break
        lt, rt = 1, 1
        while alphabet_number[idx - lt] == 0:
            lt += 1
        while alphabet_number[idx + rt] == 0:
            rt += 1
        if lt < rt:
            answer += lt
            idx -= lt
        else:
            answer += rt
            idx += rt

    return answer

name = "JABBBBCCCZC"

print(solution(name))