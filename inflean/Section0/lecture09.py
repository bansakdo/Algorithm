# 리스트와 내장함수 (2)

a = [23, 12, 36, 53, 19]
print(a[:3])
print(a[1:4])
print(len(a))

for i in range(len(a)):
    print(a[i], end=' ')
print()

for x in a:
    print(x, end=' ')
print()

for x in a:
    if x%2 == 1:
        print(x, end=' ')
print()

for x in enumerate(a):
    print(x)


b = (1, 2, 3, 4, 5)             # 튜플. 튜플은 값 변경 불가
print(b[0])

for x in enumerate(a):
    print(x[0], x[1])           # index 0: key, index 1: value
print()

for index, value in enumerate(a):
    print(index, value)
print()


if all(60 > x for x in a):
    print("YES")
else:
    print("No")

if all(1 > x for x in a):
    print("YES")
else:
    print("No")



