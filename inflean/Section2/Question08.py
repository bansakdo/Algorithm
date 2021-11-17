import sys

sys.stdin = open("input.txt", "rt")

# 8번 문제. 뒤집은 소수

# 내가 푼거
'''
def reverse(x):
    x = str(x)
    length = len(x)
    new_arr = str(0)
    for _ in range(length):
        new_arr += x[-1:]
        x = x[:-1]
    # new_arr = x[::-1]                 # 리스트 역순으로 접근.
    return int(new_arr)

def isPrime(x):
    if x == 1:
        return False
    for j in range(2, x):
        if x % j == 0:
            break
    else:
        print(x, end=' ')


n = int(input())
inputNum = [x for x in input().split()]
reversedList = list()
for i in range(n):
    reversedList.append(reverse(inputNum[i]))
for i in range(n):
    isPrime(reversedList[i])
'''

# 해설

def reverse(x):
    res = 0
    while x > 0:
        t = x % 10
        res = res * 10 + t
        x = x // 10
    return res

def isPrime(x):
    if x == 1:
        return False
    for i in range(2, x // 2 + 1):
        if x % i == 0:
            return False
    else:
        return True
n = int(input())
a = list(map(int, input().split()))
for x in a:
    tmp = reverse(x)
    if isPrime(tmp):
        print(tmp, end=' ')


