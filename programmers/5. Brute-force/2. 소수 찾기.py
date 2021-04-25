from collections import deque


# 내 풀이
# 에라토스테네스의 체 사용
# '''
def isPrime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def DFS(num_list, ch, number, primes):
    if all(ch):
        if number not in primes and isPrime(number):
            primes.append(number)
    else:
        if number not in primes and isPrime(number):
            primes.append(number)
        for i, v in enumerate(ch):
            if v == 0:
                ch[i] = 1
                use = num_list[i]
                primes = DFS(num_list, ch, int(str(number) + str(use)), primes)
                ch[i] = 0
    return primes

def solution(numbers):
    size = len(numbers)
    ch = [0] * size
    res = DFS(numbers, ch, 0, [])
    print(numbers, ":", res)
    answer = len(res)

    return answer
'''
from itertools import permutations
def solution(n):
    a = set()
    for i in range(len(n)):
        a |= set(map(int, map("".join, permutations(list(n), i + 1))))
    a -= set(range(0, 2))
    for i in range(2, int(max(a) ** 0.5) + 1):
        a -= set(range(i * 2, max(a) + 1, i))
    return len(a)
    '''

# numbers = "17"
numbers = "011"
# numbers = "0112"
# print(solution(numbers))
# print(solution("123"))
# print(solution("000"))
# print(solution("03034"))
# print(solution("0009991"))
print(solution("1111111"))

'''

'''

