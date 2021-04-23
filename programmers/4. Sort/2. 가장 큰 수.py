
# 내 풀이. 1, 2, 3, 5, 6 시간초과
'''
def solution(numbers):
    answer = ''

    for i in range(len(numbers) - 1):
        for j in range(i + 1, len(numbers)):
            num_i = str(numbers[i])
            num_j = str(numbers[j])

            cmp1 = num_i + num_j
            cmp2 = num_j + num_i
            if cmp1 < cmp2:
                numbers[i], numbers[j] = numbers[j], numbers[i]


    # print(numbers)
    for idx, x in enumerate(numbers):
        isZero = True
        if isZero and idx != len(numbers) - 1:
            if numbers[0] == 0:
                if idx == 0 or (numbers[idx - 1] == x == 0):
                    continue
            isZero = False
        answer += str(x)

    # print(answer)
    return answer

'''

# 다른사람 풀이
def solution(numbers):
    _numbers = list(map(str, numbers))
    _numbers.sort(key = lambda x: x*3, reverse=True)
    return str(int(''.join(_numbers)))


# numbers = [6, 10, 2]
# numbers = [3, 30, 34, 31, 5, 9]
numbers = [3, 90, 30, 7, 1000, 34, 5, 9, 0, 33, 90, 91]
# numbers = [0, 0, 0, 1]
# => 953433130

print(solution(numbers))