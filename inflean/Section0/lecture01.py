# 1. 변수와 출력함수

'''
    변수명 정하기
    1) 영문과 숫자, _ 로 이루어진다.
    2) 대소문자 구분
    3) 문자나 _ 로 시작
    4) 특수문자 사용 X (&, % 등)
    5) 키워드 사용 X (if, for 등)
'''

a = 1
A = 2
A1 = 3
_b = 4
print(a, A, A1, _b)

a, b, c = 3, 2, 1
print(a, b, c)

# 값교환
a, b = 10, 20
print(a, b)
a, b = b, a
print(a, b)

# 변수 타입
a = 12345
print(type(a))          # 변수 타입 출력
a = 12.1212211267567899999
print(a)
print(type(a))
a='student'
print(a)
print(type(a))

# 출력 방식
print("number")
a, b, c = 1, 2, 3
print(a, b, c)
print("number : ", a, b, c)
print(a, b, c, sep=', ')        # sep : separator
print(a, b, c, sep="\n")







