
def solution(scores):
    answer = ''
    scores = list(map(list, zip(*scores)))

    for i in range(len(scores)):
        col = scores[i]
        if col[i] in [max(col), min(col)] and col.count(col[i]) == 1:
            col.pop(i)

        average = sum(col) / len(col)

        if average >= 90:
            answer += 'A'
        elif average >= 80:
            answer += 'B'
        elif average >= 70:
            answer += 'C'
        elif average >= 50:
            answer += 'D'
        else:
            answer += 'F'
    return answer


scores = [[100,90,98,88,65],[50,45,99,85,77],[47,88,95,80,67],[61,57,100,80,65],[24,90,94,75,65]]
print(solution(scores))     # FBABD