from itertools import combinations
import math


def solution(nums):
    answer = 0

    comb = list(combinations(nums, 3))
    for c in comb:
        x = sum(c)
        for i in range(2, int(math.sqrt(x)) + 1):
            if x % i == 0:
                break
        else:
            answer += 1

    return answer


nums = [1, 2, 3, 4]
# -> 1

print(solution(nums))