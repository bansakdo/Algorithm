# 함수 만들기

# def add(a, b):            # def 키워드로 함수 선언
#     c = a + b
#     print(c)
#
# add(3, 2)

# 함수는 항상 메인 스크립트 위쪽에 선언.

# def add(a, b):
#     c = a + b
#     return c
#
# x = add(3, 2)
# print(x)


# def add(a, b):
#     c=a+b
#     d=a-b
#     return c, d             # 튜플로 리턴
#
# print(add(3, 2))


def isPrime(x):
    for i in range(2, x):
        if x % i == 0:
            return False
    return True

a=[12, 13, 7, 9, 19]
for x in a:
    if isPrime(x):
        print(x, end=' ')





