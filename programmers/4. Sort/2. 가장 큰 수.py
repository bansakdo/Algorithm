

# 다른사람 풀이
# '''
def solution(numbers):

    _numbers = list(map(str, numbers))
    _numbers.sort(key=lambda x: x*3, reverse=True)
    return str(int(''.join(_numbers)))
# '''





# numbers = [6, 10, 2]
# numbers = [3, 30, 34, 31, 5, 9]
# => 953433130
# numbers = [3, 90, 30, 7, 1000, 34, 5, 9, 0, 33, 90, 91]
# 991909075343333010000
# 991909075343333010000
numbers = [1110, 1111, 1112, 1]
numbers = [9990, 9991, 9992, 9]

print(solution(numbers))
