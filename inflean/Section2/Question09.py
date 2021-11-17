import sys

sys.stdin = open("input.txt", "rt")

# 9번 문제. 주사위 게임
# 내가 푼거
'''
n = int(input())
diceNum = [[int(x) for x in input().split()] for _ in range(n)]
highestPrice = 0

for i in range(n):
    numList = diceNum[i]
    num = 1
    val = 0
    price = 0
    if numList[0] == numList[1]:
        num += 1
        val = numList[0]
    if numList[0] == numList[2]:
        num += 1
        val = numList[0]
    if num < 3 and numList[1] == numList[2]:
        num += 1
        val = numList[1]
    if num == 1:
        numList.sort(reverse=False)
        price = numList[0] * 100
    elif num == 2:
        price = 1000 + val * 100
    elif num == 3:
        price = 10000 + val * 1000

    if highestPrice < price:
        highestPrice = price


print(highestPrice)
'''


# 해설

n = int(input())
res = 0
for i in range(n):
    tmp = input().split()
    tmp.sort()
    a, b, c = map(int, tmp)
    if a == b and b == c:
        money = 10000 + a * 1000
    elif a == b or a == c:
        money = 1000 + (a * 100)
    elif b == c:
        money = 1000 + (b * 100)
    else:
        money = c * 100
    if money > res:
        res = money
print(res )

