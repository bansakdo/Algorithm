

# 내가 푼 코드
'''
def solution(brown, yellow):
    answer = []
    yellow_area = set()
    for i in range(1, yellow // 2 + 2):
        if yellow % i == 0:
            a, b = i, yellow // i
            tmp = tuple(sorted([a, b]))
            yellow_area.add(tmp)

    yellow_area = list(yellow_area)
    for aliquots in yellow_area:
        len_col = aliquots[0] + 2
        len_row = aliquots[1] + 2
        if len_col * len_row - yellow == brown:
            answer = [len_row, len_col]
            break
    return answer
'''

# 다른사람이 푼 코드
# '''
def solution(brown, yellow):
    for i in range(1, int(yellow**(1/2))+1):
        if yellow % i == 0:
            if 2*(i + yellow//i) == brown-4:
                return [yellow//i+2, i+2]
# '''

# brown = 10
# yellow = 2
# brown = 8
# yellow = 1

brown = 24
yellow = 24

print(solution(brown, yellow))
