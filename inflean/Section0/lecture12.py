# 람다 함수 (익명의 함수, 람다 표현식)

# def plus_one(x):
#     return x+1
#
# print(plus_one(1))

# 람다함수
# plus_two = lambda x: x + 2
# print(plus_two(1))


def plus_one(x):
    return x+1

a = [1, 2, 3]
print(list(map(plus_one, a)))               # map(plus_one, a)는 a를 plus_one 함수에 적용하는 것.
print(list(map(lambda x: x+1, a)))

# sort 할 때 많이 사용.


