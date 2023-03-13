import itertools

def solution(nums):
    answer = 0

    kind_num = int(len(nums) / 2)
    kinds = set()
    for num in nums:
        kinds.add(num)


    #itertools.combinations()

    answer = min(len(kinds), kind_num)


    return answer



nums = [3, 1, 2, 3]
nums = [3, 3, 3, 2, 2, 4]
nums = [3, 3, 3, 2, 2, 2]
print(solution(nums))
