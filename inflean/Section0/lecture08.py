z# 리스트와 내장함수 (1)
import random as r

a = []  # 빈 리스트
b = list()
print(a)
print(b)

a = [1, 2, 3, 4, 5]  # 리스트 선언 동시에 초기화
print(a)
print(a[0])

b = list(range(1, 11))
print(b)

c = a + b
print(c)

print(a)
a.append(6)             # 리스트 맨 뒤에 추가
print(a)

a.insert(3, 7)          # 리스트에서 해당 인덱스에 값 추가. 3번 인덱스에 7추가
print(a)

a.pop()                 # 리스트에서 마지막 사라짐.
print(a)

a.pop(3)                # 해당 인덱스의 값 사라짐
print(a)

a.remove(4)             # 해당 값을 지움
print(a)

print(a.index(5))       # 해당 값의 인덱스 번호를 출력

a = list(range(1, 11))
print(a)
print(sum(a))           # 해당 리스트의 모든 값의 합을 출력
print(max(a))           # 해당 리스트의 모든 값 중 큰 값을 출력
print(min(a))           # 해당 리스트의 모든 값 중 작은 값을 출력
print(min(7, 5))        # 7과 5 중 작은 값 출력
print(min(7, 3, 5))     # 7과 3, 5 중 작은 값 출력

print(a)
r.shuffle(a)            # random 함수를 사용하여 리스트 안의 내용들을 무작위로 섞음
print(a)
a.sort(reverse=True)    # a를 내림차순으로 정렬
print(a)
a.sort()                # a를 오름차순으로 정렬
print(a)
a.clear()               # 리스트 비움
print(a)











