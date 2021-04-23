

# 내 풀이
'''
def DFS(numbers, target, tot):
    if len(numbers) == 0:
        if tot == target:
            return 1
        else:
            return 0
    else:
        res = 0
        res += DFS(numbers[:-1], target, tot + numbers[-1])
        res += DFS(numbers[:-1], target, tot - numbers[-1])
        return res


def solution(numbers, target):
    answer = DFS(numbers, target, 0)

    return answer
'''

# 다른사람 풀이
def solution(numbers, target):
    if not numbers and target == 0 :
        return 1
    elif not numbers:
        return 0
    else:
        return solution(numbers[1:], target-numbers[0]) + solution(numbers[1:], target+numbers[0])

numbers = [1, 1, 1, 1, 1]
target = 3

print(solution(numbers, 3))