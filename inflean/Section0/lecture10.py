# 2차 리스트 생성과 접근

a = [0] * 3         # 0인 값이 3개가 들어간 1차원 리스트
print(a)

a = [[0]*3 for _ in range(3)]       # 0인 값이 3개 들어간 1차원 리스트 3개로 이루어진 2차원 리스트
print(a)                            # [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

a[0][1] = 1
print(a)
a[1][1] = 2
print(a)

for x in a:                         # 1차원 리스트씩 출력
    print(x)

for x in a:
    for y in x:
        print(y, end=' ')
    print()

