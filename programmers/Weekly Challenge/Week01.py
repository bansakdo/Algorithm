


def solution(price, money, count):
    return -min(0, money - sum(price * i for i in range(1, count+1)))

print(solution(3, 20, 4))   # 10


